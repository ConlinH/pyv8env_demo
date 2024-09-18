from .flags import *


@construct_110001
class DOMException(Exception):
    INDEX_SIZE_ERR = 1
    DOMSTRING_SIZE_ERR = 2
    HIERARCHY_REQUEST_ERR = 3
    WRONG_DOCUMENT_ERR = 4
    INVALID_CHARACTER_ERR = 5
    NO_DATA_ALLOWED_ERR = 6
    NO_MODIFICATION_ALLOWED_ERR = 7
    NOT_FOUND_ERR = 8
    NOT_SUPPORTED_ERR = 9
    INUSE_ATTRIBUTE_ERR = 10
    INVALID_STATE_ERR = 11
    SYNTAX_ERR = 12
    INVALID_MODIFICATION_ERR = 13
    NAMESPACE_ERR = 14
    INVALID_ACCESS_ERR = 15
    VALIDATION_ERR = 16
    TYPE_MISMATCH_ERR = 17
    SECURITY_ERR = 18
    NETWORK_ERR = 19
    ABORT_ERR = 20
    URL_MISMATCH_ERR = 21
    QUOTA_EXCEEDED_ERR = 22
    TIMEOUT_ERR = 23
    INVALID_NODE_TYPE_ERR = 24
    DATA_CLONE_ERR = 25

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("code", "get_code", None, 0, 1, 0, 0, 0, 0, 1),
        ("name", "get_name", None, 0, 1, 0, 0, 0, 0, 1),
        ("message", "get_message", None, 0, 1, 0, 0, 0, 0, 1),

    )

    def get_code(self):
        val = self._attr.get('code')
        if val is not None:
            return val
        logger.info(f'patch -> v8_dom_exception.py -> DOMException.code -> get attr')

    def get_name(self):
        val = self._attr.get('name')
        if val is not None:
            return val
        logger.info(f'patch -> v8_dom_exception.py -> DOMException.name -> get attr')

    def get_message(self):
        val = self._attr.get('message')
        if val is not None:
            return val
        logger.info(f'patch -> v8_dom_exception.py -> DOMException.message -> get attr')
