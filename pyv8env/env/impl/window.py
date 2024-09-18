import time

import pyv8env
from pyv8env import Null, Undefined
from pyv8env.env.impl import *
from pyv8env.env.impl.error.base_error import V8TypeError
from pyv8env.env.impl.error.dom_exception import DOMException
# from .window_depen.dom_file_system import DOMFileSystem
from ..chrome.flags import *
from ..chrome.v8_window import Window as V8Window
from ..downloader import DownloadHandler
from ..priority_queue import MemoryPriorityQueue


@impl_warp
class Window(V8Window):

    def __v8_name_get__(self, name):
        if name in exposed_constructs:
            return exposed_constructs[name]

    def __v8_index_get__(self, *args):
        pass

    def __v8_index_set__(self, *args):
        return pyv8env.Undefined

    def __v8_index_del__(self, *args):
        pass

    def __v8_index_enum__(self, *args):
        return 0

    def __v8_index_definer__(self, *args):
        pass

    def __v8_index_desc__(self, *args):
        pass

    __v8_attribute__ = (
        ("window", "get_window", None, 0, 0, 4, 0, 1, 0, 1),
        ("self", "get_self", "set_self", 0, 0, 0, 0, 1, 0, 1),
        ("document", "get_document", None, 0, 0, 4, 0, 0, 0, 1),
        ("name", "get_name", "set_name", 0, 0, 0, 0, 0, 0, 1),
        ("location", "get_location", "set_location", 0, 0, 4, 0, 1, 1, 1),
        ("customElements", "get_customElements", None, 0, 0, 0, 0, 0, 0, 1),
        ("history", "get_history", None, 0, 0, 0, 0, 0, 0, 1),
        ("navigation", "get_navigation", "set_navigation", 0, 0, 0, 0, 0, 0, 1),
        ("locationbar", "get_locationbar", "set_locationbar", 0, 0, 0, 0, 0, 0, 1),
        ("menubar", "get_menubar", "set_menubar", 0, 0, 0, 0, 0, 0, 1),
        ("personalbar", "get_personalbar", "set_personalbar", 0, 0, 0, 0, 0, 0, 1),
        ("scrollbars", "get_scrollbars", "set_scrollbars", 0, 0, 0, 0, 0, 0, 1),
        ("statusbar", "get_statusbar", "set_statusbar", 0, 0, 0, 0, 0, 0, 1),
        ("toolbar", "get_toolbar", "set_toolbar", 0, 0, 0, 0, 0, 0, 1),
        ("status", "get_status", "set_status", 0, 0, 0, 0, 0, 0, 1),
        ("closed", "get_closed", None, 0, 0, 0, 0, 1, 0, 1),
        ("frames", "get_frames", "set_frames", 0, 0, 0, 0, 1, 0, 1),
        ("length", "get_length", "set_length", 0, 0, 0, 0, 1, 0, 1),
        ("top", "get_top", None, 0, 0, 4, 0, 1, 0, 1),
        ("opener", "get_opener", "set_opener", 0, 0, 0, 0, 1, 0, 1),
        ("parent", "get_parent", "set_parent", 0, 0, 0, 0, 1, 0, 1),
        ("frameElement", "get_frameElement", None, 0, 0, 0, 0, 0, 0, 1),
        ("navigator", "get_navigator", None, 0, 0, 0, 0, 0, 0, 1),
        ("origin", "get_origin", "set_origin", 0, 0, 0, 0, 0, 0, 1),
        ("external", "get_external", "set_external", 0, 0, 0, 0, 0, 0, 1),
        ("screen", "get_screen", "set_screen", 0, 0, 0, 0, 0, 0, 1),
        ("innerWidth", "get_innerWidth", "set_innerWidth", 0, 0, 0, 0, 0, 0, 1),
        ("innerHeight", "get_innerHeight", "set_innerHeight", 0, 0, 0, 0, 0, 0, 1),
        ("scrollX", "get_scrollX", "set_scrollX", 0, 0, 0, 0, 0, 0, 1),
        ("pageXOffset", "get_pageXOffset", "set_pageXOffset", 0, 0, 0, 0, 0, 0, 1),
        ("scrollY", "get_scrollY", "set_scrollY", 0, 0, 0, 0, 0, 0, 1),
        ("pageYOffset", "get_pageYOffset", "set_pageYOffset", 0, 0, 0, 0, 0, 0, 1),
        ("visualViewport", "get_visualViewport", "set_visualViewport", 0, 0, 0, 0, 0, 0, 1),
        ("screenX", "get_screenX", "set_screenX", 0, 0, 0, 0, 0, 0, 1),
        ("screenY", "get_screenY", "set_screenY", 0, 0, 0, 0, 0, 0, 1),
        ("outerWidth", "get_outerWidth", "set_outerWidth", 0, 0, 0, 0, 0, 0, 1),
        ("outerHeight", "get_outerHeight", "set_outerHeight", 0, 0, 0, 0, 0, 0, 1),
        ("devicePixelRatio", "get_devicePixelRatio", "set_devicePixelRatio", 0, 0, 0, 0, 0, 0, 1),
        ("event", "get_event", "set_event", 0, 0, 0, 0, 0, 0, 1),
        ("clientInformation", "get_clientInformation", "set_clientInformation", 0, 0, 0, 0, 0, 0, 1),
        ("offscreenBuffering", "get_offscreenBuffering", "set_offscreenBuffering", 0, 0, 2, 0, 0, 0, 1),
        ("screenLeft", "get_screenLeft", "set_screenLeft", 0, 0, 0, 0, 0, 0, 1),
        ("screenTop", "get_screenTop", "set_screenTop", 0, 0, 0, 0, 0, 0, 1),
        ("styleMedia", "get_styleMedia", None, 0, 0, 0, 0, 0, 0, 1),
        ("onsearch", "get_onsearch", "set_onsearch", 0, 0, 0, 0, 0, 0, 1),
        ("isSecureContext", "get_isSecureContext", None, 0, 0, 0, 0, 0, 0, 1),
        ("trustedTypes", "get_trustedTypes", None, 0, 0, 0, 0, 0, 0, 1),
        ("performance", "get_performance", "set_performance", 0, 0, 0, 0, 0, 0, 1),
        ("onappinstalled", "get_onappinstalled", "set_onappinstalled", 0, 0, 0, 0, 0, 0, 1),
        ("onbeforeinstallprompt", "get_onbeforeinstallprompt", "set_onbeforeinstallprompt", 0, 0, 0, 0, 0, 0, 1),
        ("crypto", "get_crypto", None, 0, 0, 0, 0, 0, 0, 1),
        ("indexedDB", "get_indexedDB", None, 0, 0, 0, 0, 0, 0, 1),
        ("sessionStorage", "get_sessionStorage", None, 0, 0, 0, 0, 0, 0, 1),
        ("localStorage", "get_localStorage", None, 0, 0, 0, 0, 0, 0, 1),
        ("onbeforexrselect", "get_onbeforexrselect", "set_onbeforexrselect", 0, 0, 0, 0, 0, 0, 1),
        ("onabort", "get_onabort", "set_onabort", 0, 0, 0, 0, 0, 0, 1),
        ("onbeforeinput", "get_onbeforeinput", "set_onbeforeinput", 0, 0, 0, 0, 0, 0, 1),
        ("onbeforematch", "get_onbeforematch", "set_onbeforematch", 0, 0, 0, 0, 0, 0, 1),
        ("onbeforetoggle", "get_onbeforetoggle", "set_onbeforetoggle", 0, 0, 0, 0, 0, 0, 1),
        ("onblur", "get_onblur", "set_onblur", 0, 0, 0, 0, 0, 0, 1),
        ("oncancel", "get_oncancel", "set_oncancel", 0, 0, 0, 0, 0, 0, 1),
        ("oncanplay", "get_oncanplay", "set_oncanplay", 0, 0, 0, 0, 0, 0, 1),
        ("oncanplaythrough", "get_oncanplaythrough", "set_oncanplaythrough", 0, 0, 0, 0, 0, 0, 1),
        ("onchange", "get_onchange", "set_onchange", 0, 0, 0, 0, 0, 0, 1),
        ("onclick", "get_onclick", "set_onclick", 0, 0, 0, 0, 0, 0, 1),
        ("onclose", "get_onclose", "set_onclose", 0, 0, 0, 0, 0, 0, 1),
        ("oncontentvisibilityautostatechange", "get_oncontentvisibilityautostatechange",
         "set_oncontentvisibilityautostatechange", 0, 0, 0, 0, 0, 0, 1),
        ("oncontextlost", "get_oncontextlost", "set_oncontextlost", 0, 0, 0, 0, 0, 0, 1),
        ("oncontextmenu", "get_oncontextmenu", "set_oncontextmenu", 0, 0, 0, 0, 0, 0, 1),
        ("oncontextrestored", "get_oncontextrestored", "set_oncontextrestored", 0, 0, 0, 0, 0, 0, 1),
        ("oncuechange", "get_oncuechange", "set_oncuechange", 0, 0, 0, 0, 0, 0, 1),
        ("ondblclick", "get_ondblclick", "set_ondblclick", 0, 0, 0, 0, 0, 0, 1),
        ("ondrag", "get_ondrag", "set_ondrag", 0, 0, 0, 0, 0, 0, 1),
        ("ondragend", "get_ondragend", "set_ondragend", 0, 0, 0, 0, 0, 0, 1),
        ("ondragenter", "get_ondragenter", "set_ondragenter", 0, 0, 0, 0, 0, 0, 1),
        ("ondragleave", "get_ondragleave", "set_ondragleave", 0, 0, 0, 0, 0, 0, 1),
        ("ondragover", "get_ondragover", "set_ondragover", 0, 0, 0, 0, 0, 0, 1),
        ("ondragstart", "get_ondragstart", "set_ondragstart", 0, 0, 0, 0, 0, 0, 1),
        ("ondrop", "get_ondrop", "set_ondrop", 0, 0, 0, 0, 0, 0, 1),
        ("ondurationchange", "get_ondurationchange", "set_ondurationchange", 0, 0, 0, 0, 0, 0, 1),
        ("onemptied", "get_onemptied", "set_onemptied", 0, 0, 0, 0, 0, 0, 1),
        ("onended", "get_onended", "set_onended", 0, 0, 0, 0, 0, 0, 1),
        ("onerror", "get_onerror", "set_onerror", 0, 0, 0, 0, 0, 0, 1),
        ("onfocus", "get_onfocus", "set_onfocus", 0, 0, 0, 0, 0, 0, 1),
        ("onformdata", "get_onformdata", "set_onformdata", 0, 0, 0, 0, 0, 0, 1),
        ("oninput", "get_oninput", "set_oninput", 0, 0, 0, 0, 0, 0, 1),
        ("oninvalid", "get_oninvalid", "set_oninvalid", 0, 0, 0, 0, 0, 0, 1),
        ("onkeydown", "get_onkeydown", "set_onkeydown", 0, 0, 0, 0, 0, 0, 1),
        ("onkeypress", "get_onkeypress", "set_onkeypress", 0, 0, 0, 0, 0, 0, 1),
        ("onkeyup", "get_onkeyup", "set_onkeyup", 0, 0, 0, 0, 0, 0, 1),
        ("onload", "get_onload", "set_onload", 0, 0, 0, 0, 0, 0, 1),
        ("onloadeddata", "get_onloadeddata", "set_onloadeddata", 0, 0, 0, 0, 0, 0, 1),
        ("onloadedmetadata", "get_onloadedmetadata", "set_onloadedmetadata", 0, 0, 0, 0, 0, 0, 1),
        ("onloadstart", "get_onloadstart", "set_onloadstart", 0, 0, 0, 0, 0, 0, 1),
        ("onmousedown", "get_onmousedown", "set_onmousedown", 0, 0, 0, 0, 0, 0, 1),
        ("onmouseenter", "get_onmouseenter", "set_onmouseenter", 0, 0, 0, 1, 0, 0, 1),
        ("onmouseleave", "get_onmouseleave", "set_onmouseleave", 0, 0, 0, 1, 0, 0, 1),
        ("onmousemove", "get_onmousemove", "set_onmousemove", 0, 0, 0, 0, 0, 0, 1),
        ("onmouseout", "get_onmouseout", "set_onmouseout", 0, 0, 0, 0, 0, 0, 1),
        ("onmouseover", "get_onmouseover", "set_onmouseover", 0, 0, 0, 0, 0, 0, 1),
        ("onmouseup", "get_onmouseup", "set_onmouseup", 0, 0, 0, 0, 0, 0, 1),
        ("onmousewheel", "get_onmousewheel", "set_onmousewheel", 0, 0, 0, 0, 0, 0, 1),
        ("onpause", "get_onpause", "set_onpause", 0, 0, 0, 0, 0, 0, 1),
        ("onplay", "get_onplay", "set_onplay", 0, 0, 0, 0, 0, 0, 1),
        ("onplaying", "get_onplaying", "set_onplaying", 0, 0, 0, 0, 0, 0, 1),
        ("onprogress", "get_onprogress", "set_onprogress", 0, 0, 0, 0, 0, 0, 1),
        ("onratechange", "get_onratechange", "set_onratechange", 0, 0, 0, 0, 0, 0, 1),
        ("onreset", "get_onreset", "set_onreset", 0, 0, 0, 0, 0, 0, 1),
        ("onresize", "get_onresize", "set_onresize", 0, 0, 0, 0, 0, 0, 1),
        ("onscroll", "get_onscroll", "set_onscroll", 0, 0, 0, 0, 0, 0, 1),
        ("onsecuritypolicyviolation", "get_onsecuritypolicyviolation", "set_onsecuritypolicyviolation", 0, 0, 0, 0,
         0, 0, 1),
        ("onseeked", "get_onseeked", "set_onseeked", 0, 0, 0, 0, 0, 0, 1),
        ("onseeking", "get_onseeking", "set_onseeking", 0, 0, 0, 0, 0, 0, 1),
        ("onselect", "get_onselect", "set_onselect", 0, 0, 0, 0, 0, 0, 1),
        ("onslotchange", "get_onslotchange", "set_onslotchange", 0, 0, 0, 0, 0, 0, 1),
        ("onstalled", "get_onstalled", "set_onstalled", 0, 0, 0, 0, 0, 0, 1),
        ("onsubmit", "get_onsubmit", "set_onsubmit", 0, 0, 0, 0, 0, 0, 1),
        ("onsuspend", "get_onsuspend", "set_onsuspend", 0, 0, 0, 0, 0, 0, 1),
        ("ontimeupdate", "get_ontimeupdate", "set_ontimeupdate", 0, 0, 0, 0, 0, 0, 1),
        ("ontoggle", "get_ontoggle", "set_ontoggle", 0, 0, 0, 0, 0, 0, 1),
        ("onvolumechange", "get_onvolumechange", "set_onvolumechange", 0, 0, 0, 0, 0, 0, 1),
        ("onwaiting", "get_onwaiting", "set_onwaiting", 0, 0, 0, 0, 0, 0, 1),
        ("onwebkitanimationend", "get_onwebkitanimationend", "set_onwebkitanimationend", 0, 0, 0, 0, 0, 0, 1),
        ("onwebkitanimationiteration", "get_onwebkitanimationiteration", "set_onwebkitanimationiteration", 0, 0, 0,
         0, 0, 0, 1),
        ("onwebkitanimationstart", "get_onwebkitanimationstart", "set_onwebkitanimationstart", 0, 0, 0, 0, 0, 0, 1),
        ("onwebkittransitionend", "get_onwebkittransitionend", "set_onwebkittransitionend", 0, 0, 0, 0, 0, 0, 1),
        ("onwheel", "get_onwheel", "set_onwheel", 0, 0, 0, 0, 0, 0, 1),
        ("onauxclick", "get_onauxclick", "set_onauxclick", 0, 0, 0, 0, 0, 0, 1),
        ("ongotpointercapture", "get_ongotpointercapture", "set_ongotpointercapture", 0, 0, 0, 0, 0, 0, 1),
        ("onlostpointercapture", "get_onlostpointercapture", "set_onlostpointercapture", 0, 0, 0, 0, 0, 0, 1),
        ("onpointerdown", "get_onpointerdown", "set_onpointerdown", 0, 0, 0, 0, 0, 0, 1),
        ("onpointermove", "get_onpointermove", "set_onpointermove", 0, 0, 0, 0, 0, 0, 1),
        ("onpointerrawupdate", "get_onpointerrawupdate", "set_onpointerrawupdate", 0, 0, 0, 0, 0, 0, 1),
        ("onpointerup", "get_onpointerup", "set_onpointerup", 0, 0, 0, 0, 0, 0, 1),
        ("onpointercancel", "get_onpointercancel", "set_onpointercancel", 0, 0, 0, 0, 0, 0, 1),
        ("onpointerover", "get_onpointerover", "set_onpointerover", 0, 0, 0, 0, 0, 0, 1),
        ("onpointerout", "get_onpointerout", "set_onpointerout", 0, 0, 0, 0, 0, 0, 1),
        ("onpointerenter", "get_onpointerenter", "set_onpointerenter", 0, 0, 0, 0, 0, 0, 1),
        ("onpointerleave", "get_onpointerleave", "set_onpointerleave", 0, 0, 0, 0, 0, 0, 1),
        ("onselectstart", "get_onselectstart", "set_onselectstart", 0, 0, 0, 0, 0, 0, 1),
        ("onselectionchange", "get_onselectionchange", "set_onselectionchange", 0, 0, 0, 0, 0, 0, 1),
        ("onanimationend", "get_onanimationend", "set_onanimationend", 0, 0, 0, 0, 0, 0, 1),
        ("onanimationiteration", "get_onanimationiteration", "set_onanimationiteration", 0, 0, 0, 0, 0, 0, 1),
        ("onanimationstart", "get_onanimationstart", "set_onanimationstart", 0, 0, 0, 0, 0, 0, 1),
        ("ontransitionrun", "get_ontransitionrun", "set_ontransitionrun", 0, 0, 0, 0, 0, 0, 1),
        ("ontransitionstart", "get_ontransitionstart", "set_ontransitionstart", 0, 0, 0, 0, 0, 0, 1),
        ("ontransitionend", "get_ontransitionend", "set_ontransitionend", 0, 0, 0, 0, 0, 0, 1),
        ("ontransitioncancel", "get_ontransitioncancel", "set_ontransitioncancel", 0, 0, 0, 0, 0, 0, 1),
        ("onafterprint", "get_onafterprint", "set_onafterprint", 0, 0, 0, 0, 0, 0, 1),
        ("onbeforeprint", "get_onbeforeprint", "set_onbeforeprint", 0, 0, 0, 0, 0, 0, 1),
        ("onbeforeunload", "get_onbeforeunload", "set_onbeforeunload", 0, 0, 0, 0, 0, 0, 1),
        ("onhashchange", "get_onhashchange", "set_onhashchange", 0, 0, 0, 0, 0, 0, 1),
        ("onlanguagechange", "get_onlanguagechange", "set_onlanguagechange", 0, 0, 0, 0, 0, 0, 1),
        ("onmessage", "get_onmessage", "set_onmessage", 0, 0, 0, 0, 0, 0, 1),
        ("onmessageerror", "get_onmessageerror", "set_onmessageerror", 0, 0, 0, 0, 0, 0, 1),
        ("onoffline", "get_onoffline", "set_onoffline", 0, 0, 0, 0, 0, 0, 1),
        ("ononline", "get_ononline", "set_ononline", 0, 0, 0, 0, 0, 0, 1),
        ("onpagehide", "get_onpagehide", "set_onpagehide", 0, 0, 0, 0, 0, 0, 1),
        ("onpageshow", "get_onpageshow", "set_onpageshow", 0, 0, 0, 0, 0, 0, 1),
        ("onpopstate", "get_onpopstate", "set_onpopstate", 0, 0, 0, 0, 0, 0, 1),
        ("onrejectionhandled", "get_onrejectionhandled", "set_onrejectionhandled", 0, 0, 0, 0, 0, 0, 1),
        ("onstorage", "get_onstorage", "set_onstorage", 0, 0, 0, 0, 0, 0, 1),
        ("onunhandledrejection", "get_onunhandledrejection", "set_onunhandledrejection", 0, 0, 0, 0, 0, 0, 1),
        ("onunload", "get_onunload", "set_onunload", 0, 0, 0, 0, 0, 0, 1),
        ("crossOriginIsolated", "get_crossOriginIsolated", None, 0, 0, 0, 0, 0, 0, 1),
        ("scheduler", "get_scheduler", "set_scheduler", 0, 0, 0, 0, 0, 0, 1),
        ("originAgentCluster", "get_originAgentCluster", None, 0, 0, 0, 0, 0, 0, 1),
        # ("onorientationchange", "get_onorientationchange", "set_onorientationchange", 0, 0, 0, 0, 0, 0, 1),
        # ("orientation", "get_orientation", None, 0, 0, 0, 0, 0, 0, 1),
        ("onpageswap", "get_onpageswap", "set_onpageswap", 0, 0, 0, 0, 0, 0, 1),
        ("onpagereveal", "get_onpagereveal", "set_onpagereveal", 0, 0, 0, 0, 0, 0, 1),
        # ("defaultStatus", "get_defaultStatus", "set_defaultStatus", 0, 0, 0, 0, 0, 0, 1),
        # ("defaultstatus", "get_defaultstatus", "set_defaultstatus", 0, 0, 0, 0, 0, 0, 1),
        ("credentialless", "get_credentialless", None, 0, 0, 0, 0, 0, 0, 1),
        # ("ai", "get_ai", "set_ai", 0, 0, 0, 0, 0, 0, 1),
        # ("model", "get_model", "set_model", 0, 0, 0, 0, 0, 0, 1),
        ("speechSynthesis", "get_speechSynthesis", None, 0, 0, 0, 0, 0, 0, 1),
        # ("onfencedtreeclick", "get_onfencedtreeclick", "set_onfencedtreeclick", 0, 0, 0, 0, 0, 0, 1),
        # ("onoverscroll", "get_onoverscroll", "set_onoverscroll", 0, 0, 0, 0, 0, 0, 1),
        ("onscrollend", "get_onscrollend", "set_onscrollend", 0, 0, 0, 0, 0, 0, 1),
        # ("onscrollsnapchange", "get_onscrollsnapchange", "set_onscrollsnapchange", 0, 0, 0, 0, 0, 0, 1),
        # ("onscrollsnapchanging", "get_onscrollsnapchanging", "set_onscrollsnapchanging", 0, 0, 0, 0, 0, 0, 1),
        # ("onmove", "get_onmove", "set_onmove", 0, 0, 0, 0, 0, 0, 1),
        # ("ontimezonechange", "get_ontimezonechange", "set_ontimezonechange", 0, 0, 0, 0, 0, 0, 1),
        # ("crossOriginEmbedderPolicy", "get_crossOriginEmbedderPolicy", None, 0, 0, 0, 0, 0, 0, 1),
        # ("translation", "get_translation", "set_translation", 0, 0, 0, 0, 0, 0, 1),
        ("fence", "get_fence", None, 0, 0, 0, 0, 0, 0, 1),
        # ("testOriginTrialGlobalAttribute", "get_testOriginTrialGlobalAttribute", None, 0, 0, 0, 0, 0, 0, 1),
        ("caches", "get_caches", None, 0, 0, 0, 0, 0, 0, 1),
        ("cookieStore", "get_cookieStore", None, 0, 0, 0, 0, 0, 0, 1),
        ("ondevicemotion", "get_ondevicemotion", "set_ondevicemotion", 0, 0, 0, 0, 0, 0, 1),
        ("ondeviceorientation", "get_ondeviceorientation", "set_ondeviceorientation", 0, 0, 0, 0, 0, 0, 1),
        ("ondeviceorientationabsolute", "get_ondeviceorientationabsolute", "set_ondeviceorientationabsolute", 0, 0,
         0, 0, 0, 0, 1),
        ("launchQueue", "get_launchQueue", None, 0, 0, 0, 0, 0, 0, 1),
        # ("privateAttribution", "get_privateAttribution", "set_privateAttribution", 0, 0, 0, 0, 0, 0, 1),
        ("sharedStorage", "get_sharedStorage", None, 0, 0, 0, 0, 0, 0, 1),
        ("documentPictureInPicture", "get_documentPictureInPicture", None, 0, 0, 0, 0, 0, 0, 1),
        # ("ontouchcancel", "get_ontouchcancel", "set_ontouchcancel", 0, 0, 0, 0, 0, 0, 1),
        # ("ontouchend", "get_ontouchend", "set_ontouchend", 0, 0, 0, 0, 0, 0, 1),
        # ("ontouchmove", "get_ontouchmove", "set_ontouchmove", 0, 0, 0, 0, 0, 0, 1),
        # ("ontouchstart", "get_ontouchstart", "set_ontouchstart", 0, 0, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        ("alert", "fn_alert", 0, 0, 0, 0, 0, 0, 0),
        ("atob", "fn_atob", 1, 0, 0, 0, 0, 0, 0),
        ("blur", "fn_blur", 0, 0, 0, 0, 0, 1, 0),
        ("btoa", "fn_btoa", 1, 0, 0, 0, 0, 0, 0),
        ("cancelAnimationFrame", "fn_cancelAnimationFrame", 1, 0, 0, 0, 0, 0, 0),
        ("cancelIdleCallback", "fn_cancelIdleCallback", 1, 0, 0, 0, 0, 0, 0),
        ("captureEvents", "fn_captureEvents", 0, 0, 0, 0, 0, 0, 0),
        ("clearInterval", "fn_clearInterval", 0, 0, 0, 0, 0, 0, 0),
        ("clearTimeout", "fn_clearTimeout", 0, 0, 0, 0, 0, 0, 0),
        ("close", "fn_close", 0, 0, 0, 0, 0, 1, 0),
        ("confirm", "fn_confirm", 0, 0, 0, 0, 0, 0, 0),
        ("createImageBitmap", "fn_createImageBitmap", 1, 0, 0, 0, 1, 0, 0),
        ("fetch", "fn_fetch", 1, 0, 0, 0, 1, 0, 0),
        ("find", "fn_find", 0, 0, 0, 0, 0, 0, 0),
        ("focus", "fn_focus", 0, 0, 0, 0, 0, 1, 0),
        ("getComputedStyle", "fn_getComputedStyle", 1, 0, 0, 0, 0, 0, 1),
        ("getSelection", "fn_getSelection", 0, 0, 0, 0, 0, 0, 1),
        ("matchMedia", "fn_matchMedia", 1, 0, 0, 0, 0, 0, 0),
        ("moveBy", "fn_moveBy", 2, 0, 0, 0, 0, 0, 0),
        ("moveTo", "fn_moveTo", 2, 0, 0, 0, 0, 0, 0),
        ("open", "fn_open", 0, 0, 0, 0, 0, 0, 0),
        ("postMessage", "fn_postMessage", 1, 0, 0, 0, 0, 1, 0),
        ("print", "fn_print", 0, 0, 0, 0, 0, 0, 0),
        ("prompt", "fn_prompt", 0, 0, 0, 0, 0, 0, 0),
        ("queueMicrotask", "fn_queueMicrotask", 1, 0, 0, 0, 0, 0, 0),
        ("releaseEvents", "fn_releaseEvents", 0, 0, 0, 0, 0, 0, 0),
        ("reportError", "fn_reportError", 1, 0, 0, 0, 0, 0, 0),
        ("requestAnimationFrame", "fn_requestAnimationFrame", 1, 0, 0, 0, 0, 0, 0),
        ("requestIdleCallback", "fn_requestIdleCallback", 1, 0, 0, 0, 0, 0, 0),
        ("resizeBy", "fn_resizeBy", 2, 0, 0, 0, 0, 0, 0),
        ("resizeTo", "fn_resizeTo", 2, 0, 0, 0, 0, 0, 0),
        ("scroll", "fn_scroll", 0, 0, 0, 0, 0, 0, 0),
        ("scrollBy", "fn_scrollBy", 0, 0, 0, 0, 0, 0, 0),
        ("scrollTo", "fn_scrollTo", 0, 0, 0, 0, 0, 0, 0),
        ("setInterval", "fn_setInterval", 1, 0, 0, 0, 0, 0, 0),
        ("setTimeout", "fn_setTimeout", 1, 0, 0, 0, 0, 0, 0),
        ("stop", "fn_stop", 0, 0, 0, 0, 0, 0, 0),
        ("structuredClone", "fn_structuredClone", 1, 0, 0, 0, 0, 0, 0),
        ("webkitCancelAnimationFrame", "fn_webkitCancelAnimationFrame", 1, 0, 0, 0, 0, 0, 0),
        ("webkitRequestAnimationFrame", "fn_webkitRequestAnimationFrame", 1, 0, 0, 0, 0, 0, 0),
        # ("getComputedAccessibleNode", "fn_getComputedAccessibleNode", 1, 0, 0, 0, 1, 0, 0),
        ("webkitRequestFileSystem", "fn_webkitRequestFileSystem", 3, 0, 0, 0, 0, 0, 0),
        ("webkitResolveLocalFileSystemURL", "fn_webkitResolveLocalFileSystemURL", 2, 0, 0, 0, 0, 0, 0),
        # ("fetchLater", "fn_fetchLater", 1, 0, 0, 0, 0, 0, 0),
        # ("getDigitalGoodsService", "fn_getDigitalGoodsService", 1, 0, 0, 0, 1, 0, 0),
        # ("getLockScreenData", "fn_getLockScreenData", 0, 0, 0, 0, 1, 0, 0),
        # ("getScreenDetails", "fn_getScreenDetails", 0, 0, 0, 0, 1, 0, 0),
        # ("maximize", "fn_maximize", 0, 0, 0, 0, 1, 0, 0),
        # ("minimize", "fn_minimize", 0, 0, 0, 0, 1, 0, 0),
        # ("restore", "fn_restore", 0, 0, 0, 0, 1, 0, 0),
        # ("setResizable", "fn_setResizable", 1, 0, 0, 0, 1, 0, 0),
        # ("openDatabase", "fn_openDatabase", 4, 0, 0, 0, 0, 0, 0),
        # ("queryLocalFonts", "fn_queryLocalFonts", 0, 0, 0, 0, 1, 0, 0),
        # ("showDirectoryPicker", "fn_showDirectoryPicker", 0, 0, 0, 0, 1, 0, 0),
        # ("showOpenFilePicker", "fn_showOpenFilePicker", 0, 0, 0, 0, 1, 0, 0),
        # ("showSaveFilePicker", "fn_showSaveFilePicker", 0, 0, 0, 0, 1, 0, 0),

    )

    def get_window(self):
        return self

    def get_top(self):
        return self

    def get_frames(self):
        return self

    def get_self(self):
        return self

    def get_parent(self):
        return self

    # def get_origin(self):
    #     return self._location.get_origin()

    # def fn_matchMedia(self, *args):
    #     if len(args) == 0:
    #         raise V8TypeError(
    #             f"Failed to execute 'matchMedia' on 'Window': 1 arguments required, but only 0 present."
    #         )
    #     return MediaQueryList(args[0])

    # def fn_webkitRequestFileSystem(self, *args, delay=True):
    #     # 文件存储系统 类似缓存 非标准接口
    #     if len(args) < 3:
    #         raise V8TypeError(
    #             f"Failed to execute 'webkitRequestFileSystem' on 'Window': 3 arguments required, but only {len(args)} present."
    #         )
    #     if args[0] not in (0, 1):
    #         if len(args) >= 3:
    #             failed_cb = args[3]
    #             failed_cb(DOMException(
    #                 "It was determined that certain files are unsafe for access within a Web application, or that "
    #                 "too many calls are being made on file resources.",
    #                 "SecurityError",
    #                 18
    #             ))
    #     # logger.debug(args)

    #     success_cb = args[3]
    #     success_cb(DOMFileSystem())


    def fn_clearTimeout(self, *args):
        if len(args) >= 1:
            del self._timers[args[0]]

    def fn_clearInterval(self, *args):
        if len(args) >= 1:
            del self._timers[args[0]]

    def fn_setTimeout(self, *args):
        self._timer_index += 1
        if len(args) == 0:
            raise V8TypeError("Failed to execute 'setTimeout' on 'Window': 1 argument required, but only 0 present.")
        delay = 0
        arguments = []
        if len(args) == 2:
            delay = args[1]
        if len(args) >= 3:
            arguments = args[2:]
        self._timers[self._timer_index] = {
            "delay": delay,
            "type": 'Timeout',
            "start": int(time.time() * 1000),
            "func": args[0],
            "arguments": arguments
        }
        return self._timer_index

    def fn_setInterval(self, *args):
        self._timer_index += 1
        if len(args) == 0:
            raise V8TypeError("Failed to execute 'setInterval' on 'Window': 1 argument required, but only 0 present.")
        delay = 0
        arguments = []
        if len(args) == 2:
            delay = args[1]
        if len(args) >= 3:
            arguments = args[2:]
        self._timers[self._timer_index] = {
            "delay": delay,
            "type": 'Interval',
            "start": int(time.time() * 1000),
            "func": args[0],
            "arguments": arguments
        }
        return self._timer_index

    def start(self, devtool=False, callback=None):
        code = """
            delete SharedArrayBuffer;
        """
        if self._hook:
            code += "faker.hook=true;"
        self.ctx.exec_js(code)

        if devtool:
            from pyv8env import start_devtools
            # start_devtools(self.ctx, True, callback=callback if callback else self.get_document().render_html)
            start_devtools(self.ctx, True, callback=callback)
        else:
            if callback:
                callback(self.ctx)
            else:
                # self.get_document().render_html(self.ctx)
                pass


    def exec_timeout(self):
        flag = True
        while flag:
            flag = False
            for index in list(self._timers.keys()):
                now = int(time.time() * 1000)
                task = self._timers[index]

                if self._timers[index]["start"] + self._timers[index]["delay"] > now:
                    logger.debug(f"----{index} pass -> {task}")
                    continue

                logger.debug(f"----{index} do -> {task}")
                flag = True
                if isinstance(task["func"], str):
                    self.ctx.exec_js(task["func"])
                else:
                    task["func"](*task["arguments"])

                if task["type"] == "Timeout":
                    del self._timers[index]
                else:
                    task["start"] = now
                    task["times"] = task.get("times", 0) + 1

    # def get_cookies(self):
    #     return self.get_document()._cookies

    def __init__(
            self,
            hook: bool = False,
            url: str = None,
            cookies: dict = None,
            html: str = None,
            download_handler: DownloadHandler = None,
            **kw
    ):
        self._hook = hook
        self._download_handler = download_handler
        if download_handler is not None:
            cookies = cookies or {}
            html = download_handler.html()
            cookies.update(download_handler.cookies)

        if html is None:
            html = '<!doctype html><html><head></head><body></body></html>'

        if url is None:
            url = 'https://www.xxx.com'

        # self._location = Location(url)
        # self._navigator = Navigator(window=self)
        for key, val in {
            # "location": self._location,
            # "document": HTMLDocument(location=self._location, html=html, cookies=cookies, referrer=url, window=self),
            # "navigator": self._navigator,
            # "customElements": CustomElementRegistry(),
            # "history": History(),
            # "navigation": Navigation(),
            # "indexedDB": IDBFactory(self),
            # "sessionStorage": Storage(),
            # "localStorage": Storage(),
            # "screen": Screen(),

            "outerWidth": 1920, "outerHeight": 1032, "innerWidth": 1872, "innerHeight": 956, "scrollX": 0,
            "pageXOffset": 0, "scrollY": 0, "pageYOffset": 0, "length": 0, "screenX": 0, "screenY": 0,
            "screenLeft": 0, "screenTop": 0,
            "devicePixelRatio": 1,

            # "locationbar": BarProp(), "menubar": BarProp(), "personalbar": BarProp(), "scrollbars": BarProp(),
            # "statusbar": BarProp(), "toolbar": BarProp(),
            "status": "",
            "name": "",
            "closed": False,
            "opener": Null, "frameElement": Null,
            # "external": External(),
            # "visualViewport": VisualViewport(),
            # "clientInformation": self._navigator,
            # "styleMedia": StyleMedia(),
            "isSecureContext": True,
            # "trustedTypes": TrustedTypePolicyFactory(),
            # "performance": Performance(),
            # "crypto": Crypto(),
            # "launchQueue": LaunchQueue(),
            # "sharedStorage": SharedStorage(),
            # "documentPictureInPicture": DocumentPictureInPicture(),
            "originAgentCluster": True,
            "credentialless": False,
            # "speechSynthesis": SpeechSynthesis(),
            "crossOriginIsolated": False,
            # "scheduler": Scheduler(),
            # "caches": CacheStorage(),
            # "cookieStore": CookieStore(),
            "onbeforeinstallprompt": Null, "onbeforexrselect": Null, "onabort": Null, "onbeforeinput": Null,
            "onbeforetoggle": Null, "onblur": Null, "oncancel": Null, "oncanplay": Null, "oncanplaythrough": Null,
            "onchange": Null, "onclick": Null, "onclose": Null, "oncontextlost": Null, "oncontextmenu": Null,
            "ondblclick": Null, "ondrag": Null, "ondragend": Null, "ondragenter": Null, "ondragleave": Null,
            "ondragover": Null, "ondragstart": Null, "ondrop": Null, "ondurationchange": Null, "onemptied": Null,
            "onended": Null, "onerror": Null,
            "onfocus": Null, "onformdata": Null, "oninput": Null, "oninvalid": Null,
            "onkeydown": Null, "onkeypress": Null, "onkeyup": Null, "onload": Null, "onloadeddata": Null,
            "onloadedmetadata": Null, "onloadstart": Null, "onmousedown": Null, "onmouseenter": Null, "onsearch": Null,
            "onmouseleave": Null, "onmousemove": Null, "onmouseout": Null, "onmouseover": Null, "onmouseup": Null,
            "onmousewheel": Null, "onpause": Null, "onplay": Null, "onplaying": Null, "onprogress": Null,
            "onratechange": Null, "onreset": Null, "onresize": Null, "onscroll": Null, "onappinstalled": Null,
            "onsecuritypolicyviolation": Null, "onseeked": Null, "onseeking": Null, "onselect": Null,
            "onslotchange": Null, "onstalled": Null, "onsubmit": Null, "onsuspend": Null, "ontimeupdate": Null,
            "ontoggle": Null, "onvolumechange": Null, "onwaiting": Null, "onwebkitanimationend": Null,
            "onwebkitanimationiteration": Null, "onwebkitanimationstart": Null, "onwebkittransitionend": Null,
            "onwheel": Null, "onauxclick": Null, "ongotpointercapture": Null, "onlostpointercapture": Null,
            "onpointerdown": Null, "onpointermove": Null, "onpointerrawupdate": Null, "onpointerup": Null,
            "onpointercancel": Null, "onpointerover": Null, "onpointerout": Null, "onpointerenter": Null,
            "onpointerleave": Null, "onselectstart": Null, "onselectionchange": Null, "onanimationend": Null,
            "onanimationiteration": Null, "onanimationstart": Null, "ontransitionrun": Null, "ontransitionstart": Null,
            "ontransitionend": Null, "ontransitioncancel": Null, "onafterprint": Null, "onbeforeprint": Null,
            "onbeforeunload": Null, "onhashchange": Null, "onlanguagechange": Null, "onmessage": Null,
            "onmessageerror": Null, "onoffline": Null, "onpagehide": Null, "onpageshow": Null, "onscrollend": Null,
            "onpopstate": Null, "onrejectionhandled": Null, "onstorage": Null, "onunhandledrejection": Null,
            "onunload": Null, "onpageswap": Null, "onpagereveal": Null, "fence": Null, "onbeforematch": Null,
            "ondevicemotion": Null, "ondeviceorientation": Null, "ondeviceorientationabsolute": Null, "ononline": Null,
            "oncontentvisibilityautostatechange": Null, "oncuechange": Null, "oncontextrestored": Null,
        }.items():
            kw.setdefault(key, val)

        super(Window, self).__init__(**kw)

        self._timers = {}
        self._timer_index = 0

        self._on_finish_tasks = MemoryPriorityQueue()

        pyv8env.Context(global_this=self, hook=hook)
