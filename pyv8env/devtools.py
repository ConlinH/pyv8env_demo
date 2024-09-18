import json
import signal

import gevent
import gevent.lock
import gevent.queue
from gevent import pywsgi
from geventwebsocket.exceptions import WebSocketError
from geventwebsocket.handler import WebSocketHandler

from pyv8env import _pyv8env


class DevtoolsDebugger(_pyv8env.Debugger):
    def __init__(self, context, *args, callback=None):
        super().__init__(context)
        self.connect_lock = gevent.lock.Semaphore(0)
        self.queues = []
        self.context = context
        self.startup_lock = gevent.lock.Semaphore(0)
        self.ws = None
        self.callback = callback
        self.args = args

        signal.signal(signal.SIGTERM, self._signal_shutdown)
        signal.signal(signal.SIGINT, self._signal_shutdown)
        if hasattr(signal, 'SIGBREAK'):
            signal.signal(signal.SIGBREAK, self._signal_shutdown)

    def _signal_shutdown(self, signum, _) -> None:
        self.connect_lock.release()

    def __call__(self, environ, start_response):
        if environ['PATH_INFO'] == '/':
            if self.ws is not None:
                print('Stop and start again')
                return []

            self.ws = environ['wsgi.websocket']
            gevent.spawn(self.run_loop)
            self.startup_lock.acquire()
            assert len(self.queues) == 1
            while True:
                try:
                    message = self.ws.receive()
                except WebSocketError:
                    break
                message = json.loads(message)
                self.top_queue.put(message)
            self.ws = None

            return []
        return []

    def handle(self, message):
        self.ws.send(json.dumps(message))

    def run_js(self):
        if self.callback:
            self.callback(self.context, *self.args)
        else:
            def print_hello():
                print("Hello pyv8env! in python")
                return "Hello pyv8env! in v8"

            self.context.expose(print_hello)
            self.context.run_js("console.log(print_hello());", 'test.js')

    def run_loop(self):
        queue = gevent.queue.Queue()
        self.queues.append(queue)
        self.startup_lock.release()
        for message in queue:
            if self.top_queue is not queue:
                self.top_queue.put(message)
            else:
                self.send(message)

    def quit_loop(self):
        self.queues.pop().put(StopIteration)

    @property
    def top_queue(self):
        return self.queues[-1]

    def wait_for_connect(self):
        self.connect_lock.wait()


def start_devtools(context, *args, callback=None, port=9005):
    debugger = DevtoolsDebugger(context, *args, callback=callback)
    server = pywsgi.WSGIServer(('localhost', port), debugger, handler_class=WebSocketHandler)
    server.start()
    print('打开浏览器的devtools， 然后在地址栏输入下列地址：')
    print('devtools://devtools/bundled/inspector.html?experiments=true&v8only=true&ws=localhost:{}'.format(port))
    debugger.wait_for_connect()


if __name__ == '__main__':
    c = _pyv8env.Context()
    start_devtools(c)
