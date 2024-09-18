from pyv8env.env.chrome.flags import *
from pyv8env.env.chrome.v8_dom_exception import DOMException as V8DOMException


@impl_warp
class DOMException(V8DOMException):
    __v8_error__ = True

    def get_code(self):
        return self._code

    def get_name(self):
        return self._name

    def get_message(self):
        return self._message

    def __init__(self, message=None, name=None, code=0, *args, **kw):
        self._name = name
        self._message = message or ''
        self._code = code
        super(DOMException, self).__init__(message)
        self._attr = {}
