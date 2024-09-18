
from pyv8env.env.impl.error.base_error import V8TypeError
from ..chrome.flags import *
from ..chrome.v8_event_target import EventTarget as V8EventTarget


@impl_warp
class EventTarget(V8EventTarget):

    __v8_method__ = (
        ("addEventListener", "fn_addEventListener", 2, 0, 1, 0, 0, 0, 0),
        ("dispatchEvent", "fn_dispatchEvent", 1, 0, 1, 0, 0, 0, 0),
        ("removeEventListener", "fn_removeEventListener", 2, 0, 1, 0, 0, 0, 0),
    )

    def fn_addEventListener(self, *args):
        logger.debug(f'{self}.addEventListener{tuple(args)}')

        if len(args) < 2:
            raise V8TypeError(
                f"Failed to execute 'addEventListener' on 'EventTarget': 2 arguments required, but only {len(args)} present."
            )
        type_ = args[0]
        listener = args[1]
        this_events = events.get(self, {})
        if not this_events:
            events[self] = this_events

        this_type_events = this_events.get(type_, [])
        if not this_type_events:
            this_events[type_] = this_type_events
        this_type_events.append(listener)

    def fn_dispatchEvent(self, *args):
        logger.debug(f'start {self}.dispatchEvent{tuple(args)}')

        if len(args) == 0:
            raise V8TypeError(
                f"Failed to execute 'dispatchEvent' on 'EventTarget': 2 arguments required, but only 0 present."
            )
        this_events = events.get(self, {})
        if not this_events:
            return

        event = args[0]
        type_ = event.get_type()
        this_type_events = this_events.get(type_, [])
        if not this_type_events:
            return
        for listener in this_type_events:
            if isinstance(listener, str):
                self.ctx.exec_js(listener)
            else:
                listener.call(self, event)
        logger.debug(f'end {self}.dispatchEvent{tuple(args)}')

    def fn_removeEventListener(self, *args):
        logger.debug(f'{self}.removeEventListener{tuple(args)}')

        if len(args) < 2:
            raise V8TypeError(
                f"Failed to execute 'removeEventListener' on 'EventTarget': 2 arguments required, but only {len(args)} present."
            )
        type_ = args[0]
        listener = args[1]
        this_events = events.get(self, {})
        if not this_events:
            return
        this_type_events = this_events.get(type_, [])
        if not this_type_events:
            return
        this_type_events.remove(listener)
