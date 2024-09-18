from .flags import *


@construct_110021
class EventTarget:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("addEventListener", "fn_addEventListener", 2, 0, 1, 0, 0, 0, 0),
        ("dispatchEvent", "fn_dispatchEvent", 1, 0, 1, 0, 0, 0, 0),
        ("removeEventListener", "fn_removeEventListener", 2, 0, 1, 0, 0, 0, 0),
        ("on", "fn_on", 1, 0, 1, 0, 0, 0, 0),

    )

    def fn_addEventListener(self, *args):
        logger.info(f'patch -> v8_event_target.py -> EventTarget.addEventListener{tuple(args)} -> method')

    def fn_dispatchEvent(self, *args):
        logger.info(f'patch -> v8_event_target.py -> EventTarget.dispatchEvent{tuple(args)} -> method')

    def fn_removeEventListener(self, *args):
        logger.info(f'patch -> v8_event_target.py -> EventTarget.removeEventListener{tuple(args)} -> method')

    def fn_on(self, *args):
        logger.info(f'patch -> v8_event_target.py -> EventTarget.on{tuple(args)} -> method')
