from pyv8env import Null
from pyv8env.env.chrome.flags import *
from pyv8env.env.chrome.v8_window_properties import WindowProperties as V8WindowProperties


@impl_warp
class WindowProperties(V8WindowProperties):

    def __v8_property_name_get__(self, name):
        try:
            ret = self.get_document().get_all().fn_namedItem(name)
            if ret is not Null:
                return ret
        except:
            pass
