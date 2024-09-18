from pyv8env.env.chrome.flags import *
from pyv8env.env.chrome.v8_dom_error import DOMError as V8DOMError
from .base_error import V8TypeError


@impl_warp
class DOMError(V8DOMError):
    __v8_error__ = True

    def get_name(self):
        return self._name

    def get_message(self):
        return self._message

    def __init__(self, name=None, message=None):
        if name is None:
            raise V8TypeError("Failed to construct 'DOMError': 1 argument required, but only 0 present")

        self._name = name
        self._message = message or ''
        super().__init__(message)
        self._attr = {}
