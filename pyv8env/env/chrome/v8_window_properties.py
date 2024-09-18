from .flags import *
from .v8_event_target import EventTarget


@construct_000020
class WindowProperties(EventTarget):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(WindowProperties, self).__init__(*args, **kw)
