import sys
from weakref import WeakKeyDictionary

from loguru import logger

logger.remove()
# logger.add(sys.stderr, format="<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green> | <level>{level: <8}</level> | <cyan>{process}</cyan> | <cyan>{name}</cyan>:<cyan>{line: <3}</cyan> | <level>{message}</level>", level="INFO")
logger.add(sys.stderr, format="<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green> | <level>{level: <8}</level> | <cyan>{process}</cyan> | <cyan>{name}</cyan>:<cyan>{line: <3}</cyan> | <level>{message}</level>", level="ERROR")
logger.add("file.log")


class CallbackType:
    kPy = 0         # 回调Python类方法
    kJs = 1         # 回调Javascript方法 例如：faker.Window_get_frames


class FlagImmutable:
    instance = 1 << 0
    prototype = 1 << 1


class V8Attribute:
    kNone = 0
    ReadOnly = 1 << 0  # ReadOnly, i.e., not writable
    DontEnum = 1 << 1  # DontEnum, i.e., not enumerable.
    DontDelete = 1 << 2  # DontDelete, i.e., not configurable


class FlagLocation:
    kInstance = 0
    kPrototype = 1
    kInterface = 2


class FlagReceiverCheck:
    kCheck = 0
    kDoNotCheck = 1


class FlagCrossOriginCheck:
    kCheck = 0
    kDoNotCheck = 1


class FlagExposed:
    kNo = 0
    kYes = 1


class FlagConstructor:
    kDontAll = 0
    kNew = 1 << 0
    kCall = 1 << 1
    kAll = kNew | kCall


class SideEffectType:
    kHasSideEffect = 0
    kHasNoSideEffect = 1
    kHasSideEffectToReceiver = 2


class FlagArrayProto:
    iterator = 1 << 0
    entries = 1 << 1
    keys = 1 << 2
    values = 1 << 3
    forEach = 1 << 4


class AttributeJSConfig:
    def __init__(
            self,
            name,
            get_cb,
            set_cb=None,
            v8_property_attribute=3,  # v8::PropertyAttribute
            location=2,  # FlagLocation
            receiver_check=1,
            cross_origin_check_for_get=1,  # FlagReceiverCheck
            cross_origin_check_for_set=1,  # FlagCrossOriginCheck
            v8_side_effect=2,  # FlagCrossOriginCheck
    ):
        self.name = name
        self.get_cb = get_cb
        self.set_cb = set_cb
        self.v8_property_attribute = v8_property_attribute
        self.location = location
        self.receiver_check = receiver_check
        self.cross_origin_check_for_get = cross_origin_check_for_get
        self.cross_origin_check_for_set = cross_origin_check_for_set
        self.v8_side_effect = v8_side_effect

    def __call__(self, func):
        setattr(func, "__v8_method__", 1)
        setattr(func, "__v8_location", self.location)
        setattr(func, "__v8_receiver_check", self.receiver_check)
        setattr(func, "__v8_cross_origin_check_for_get", self.cross_origin_check_for_get)
        setattr(func, "__v8_cross_origin_check_for_set", self.cross_origin_check_for_set)
        setattr(func, "__v8_v8_side_effect", self.v8_side_effect)


class AttributeConfig:
    def __init__(
            self,
            v8_property_attribute=V8Attribute.kNone,  # v8::PropertyAttribute
            location=FlagLocation.kPrototype,  # FlagLocation
            receiver_check=FlagReceiverCheck.kCheck,
            cross_origin_check_for_get=FlagCrossOriginCheck.kCheck,  # FlagReceiverCheck
            cross_origin_check_for_set=FlagCrossOriginCheck.kCheck,  # FlagCrossOriginCheck
            side_effect=SideEffectType.kHasSideEffect,  # FlagCrossOriginCheck
    ):
        self.property_attribute = v8_property_attribute
        self.location = location
        self.receiver_check = receiver_check
        self.cross_origin_check_for_get = cross_origin_check_for_get
        self.cross_origin_check_for_set = cross_origin_check_for_set
        self.side_effect = side_effect

    def __call__(self, func):
        setattr(func, "__v8_method__", 1)
        setattr(func, "__v8_property_attribute", self.property_attribute)
        setattr(func, "__v8_location", self.location)
        setattr(func, "__v8_receiver_check", self.receiver_check)
        setattr(func, "__v8_cross_origin_check_for_get", self.cross_origin_check_for_get)
        setattr(func, "__v8_cross_origin_check_for_set", self.cross_origin_check_for_set)
        setattr(func, "__v8_side_effect", self.side_effect)
        return func

    def __str__(self):
        return f'attr_{self.location}{self.property_attribute}{self.receiver_check}{self.cross_origin_check_for_get}{self.cross_origin_check_for_set}{self.side_effect}'


class OperationConfig:
    def __init__(
            self,
            length=0,
            v8_property_attribute=V8Attribute.kNone,
            location=FlagLocation.kPrototype,
            receiver_check=FlagReceiverCheck.kCheck,
            cross_origin_check=FlagCrossOriginCheck.kCheck,
            side_effect=SideEffectType.kHasSideEffect,
    ):
        self.length = length
        self.property_attribute = v8_property_attribute
        self.location = location
        self.receiver_check = receiver_check
        self.cross_origin_check = cross_origin_check
        self.side_effect = side_effect

    def __call__(self, func):
        setattr(func, "__v8_method", 1)
        setattr(func, "__v8_length", self.length)
        setattr(func, "__v8_property_attribute", self.property_attribute)
        setattr(func, "__v8_location", self.location)
        setattr(func, "__v8_receiver_check", self.receiver_check)
        setattr(func, "__v8_cross_origin_check", self.cross_origin_check)
        setattr(func, "__v8_side_effect", self.side_effect)
        return func

    def __str__(self):
        return f'operation_{self.location}{self.length}{self.property_attribute}{self.receiver_check}{self.cross_origin_check}{self.side_effect}'


__hook_exclude_name = (
    "dir", "dirxml", "profile", "profileEnd", "clear", "table", "keys", "values",
    "debug", "undebug", "monitor", "unmonitor", "inspect", "copy", "queryObjects",
    "$", "$$", "$_", "$0", "$1", "$2", "$3", "$4", "$", "$x", "getEventListeners", "DataVie",
    "getAccessibleName", "getAccessibleRole", "monitorEvents", "unmonitorEvents",
    "String", "Array", "Date", "Object", "window", "Symbol", "Number", "Function",
    "parseFloat", "parseInt", "Math", "BigInt", "RegExp", "console", "isNaN", "Boolean",
    "faker",
)


def __v8_get_hook__(self, name, value=None, error=None):
    if name in __hook_exclude_name:
        return
    msg = f"getter: {self.__class__.__name__}.{name} -> {value}"
    if error:
        msg += f", error: {error}"
    logger.info(msg)


def __v8_set_hook__(self, name, value, error):
    msg = f"setter: {self.__class__.__name__}.{name} = {value}"
    if error:
        msg += f", error: {error}"
    logger.info(msg)


def __v8_method_hook__(self, func_name, arguments, value, has_error):
    msg = f"method: {self.__class__.__name__}.{func_name}{tuple(arguments)}"
    if has_error:
        msg += f" -> error: {value}"
    else:
        msg += f" -> {value}"
    logger.info(msg)


def __v8_construct_hook__(name, arguments, value, has_error, is_construct_call):
    if is_construct_call:
        msg = f"construct: new {name}{tuple(arguments)} -> {value}"
    else:
        msg = f"construct: {name}{tuple(arguments)} -> {value}"
    if has_error:
        msg += f", has_error: {has_error}"
    logger.info(msg)


exposed_constructs = {}


class ConstructorConfig:
    def __init__(
            self,
            exposed=FlagExposed.kYes,
            constructor=FlagConstructor.kDontAll,
            length=0,
            v8_array=0,  # FlagArrayProto
            immutable=0,
            has_constructor=1,
            hook=True,
    ):
        self.exposed = exposed
        self.constructor = constructor
        self.length = length
        self.hook = hook
        self.v8_array = v8_array
        self.immutable = immutable
        self.has_constructor = has_constructor

    def __call__(self, cls):
        if self.exposed == FlagExposed.kYes:
            exposed_constructs[cls.__name__] = cls
        setattr(cls, "__v8_constructor__", self.constructor)
        setattr(cls, "__v8_length__", self.length)
        setattr(cls, "__v8_array__", self.v8_array)
        setattr(cls, "__v8_immutable__", self.immutable)
        setattr(cls, "__v8_has_constructor__", self.has_constructor)
        if self.hook:
            cls.__v8_get_hook__ = __v8_get_hook__
            cls.__v8_set_hook__ = __v8_set_hook__
            cls.__v8_method_hook__ = __v8_method_hook__
            cls.__v8_construct_hook__ = __v8_construct_hook__
        return cls

    def __str__(self):
        return f'construct_{self.exposed}{self.constructor}{self.length}{int(self.v8_array)}{int(self.immutable)}{int(self.has_constructor)}'


def impl_warp(cls):
    father = cls.__base__
    for name in cls.__dict__:
        if name == '__module__':
            continue
        setattr(father, name, cls.__dict__[name])
    return father


events = WeakKeyDictionary()
