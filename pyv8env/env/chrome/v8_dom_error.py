from .flags import *


@construct_111001
class DOMError(Exception):

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("name", "get_name", None, 0, 1, 0, 0, 0, 0, 1),
        ("message", "get_message", None, 0, 1, 0, 0, 0, 0, 1),

    )

    def get_name(self):
        val = self._attr.get('name')
        if val is not None:
            return val
        logger.info(f'patch -> v8_dom_error.py -> DOMError.name -> get attr')

    def get_message(self):
        val = self._attr.get('message')
        if val is not None:
            return val
        logger.info(f'patch -> v8_dom_error.py -> DOMError.message -> get attr')
