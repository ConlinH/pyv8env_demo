
class V8Error(Exception):
    __v8_error__ = True


class V8TypeError(TypeError):
    __v8_error__ = True


class V8RangeError(Exception):
    __v8_error__ = True


class V8ReferenceError(ReferenceError):
    __v8_error__ = True


class V8SyntaxError(SyntaxError):
    __v8_error__ = True
