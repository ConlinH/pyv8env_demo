from pyv8env import _pyv8env


_pyv8env.init_v8(
    icudtl_path=r'icudtl.dat',
    # params=[
    #     # "--no-freeze-flags-after-init",
    #     # "--max_old_space_size=8096",
    #     # "--max-shared-heap-size=4024",
    #     # "--max_semi_space_size=8096",
    #     # "--initial-shared-heap-size=4024",
    #     # "--single-threaded",
    #     "--allow-natives-syntax"
    # ]
)

Context = _pyv8env.Context
Script = _pyv8env.Script
Debugger = _pyv8env.Debugger
JSObject = _pyv8env.JSObject
JSPromise = _pyv8env.JSPromise
JSFunction = _pyv8env.JSFunction
JSException = _pyv8env.JSException
JavaScriptTerminated = _pyv8env.JavaScriptTerminated
Null = _pyv8env.Null
Undefined = _pyv8env.Undefined
current_context = _pyv8env.current_context
new = _pyv8env.new

from .debug import Debugger, DebuggerError
from .devtools import start_devtools
