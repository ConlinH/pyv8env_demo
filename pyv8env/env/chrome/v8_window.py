from .flags import *
from .v8_window_properties import WindowProperties


@construct_100031
class Window(WindowProperties):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(Window, self).__init__(*args, **kw)
    TEMPORARY = 0
    PERSISTENT = 1

    def __v8_index_get__(self, *args):
        logger.info('patch -> v8_window.py -> Window.__v8_index_get__')
            
    def __v8_index_set__(self, *args):
        logger.info('patch -> v8_window.py -> Window.__v8_index_set__')
            
    def __v8_index_del__(self, *args):
        logger.info('patch -> v8_window.py -> Window.__v8_index_del__')
            
    def __v8_index_enum__(self, *args):
        logger.info('patch -> v8_window.py -> Window.__v8_index_enum__')
            
    def __v8_index_definer__(self, *args):
        logger.info('patch -> v8_window.py -> Window.__v8_index_definer__')
            
    def __v8_index_desc__(self, *args):
        logger.info('patch -> v8_window.py -> Window.__v8_index_desc__')
            
    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
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
        ("oncontentvisibilityautostatechange", "get_oncontentvisibilityautostatechange", "set_oncontentvisibilityautostatechange", 0, 0, 0, 0, 0, 0, 1),
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
        ("onsecuritypolicyviolation", "get_onsecuritypolicyviolation", "set_onsecuritypolicyviolation", 0, 0, 0, 0, 0, 0, 1),
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
        ("onwebkitanimationiteration", "get_onwebkitanimationiteration", "set_onwebkitanimationiteration", 0, 0, 0, 0, 0, 0, 1),
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
        ("onorientationchange", "get_onorientationchange", "set_onorientationchange", 0, 0, 0, 0, 0, 0, 1),
        ("orientation", "get_orientation", None, 0, 0, 0, 0, 0, 0, 1),
        ("onpageswap", "get_onpageswap", "set_onpageswap", 0, 0, 0, 0, 0, 0, 1),
        ("onpagereveal", "get_onpagereveal", "set_onpagereveal", 0, 0, 0, 0, 0, 0, 1),
        ("defaultStatus", "get_defaultStatus", "set_defaultStatus", 0, 0, 0, 0, 0, 0, 1),
        ("defaultstatus", "get_defaultstatus", "set_defaultstatus", 0, 0, 0, 0, 0, 0, 1),
        ("credentialless", "get_credentialless", None, 0, 0, 0, 0, 0, 0, 1),
        ("ai", "get_ai", "set_ai", 0, 0, 0, 0, 0, 0, 1),
        ("model", "get_model", "set_model", 0, 0, 0, 0, 0, 0, 1),
        ("speechSynthesis", "get_speechSynthesis", None, 0, 0, 0, 0, 0, 0, 1),
        ("onfencedtreeclick", "get_onfencedtreeclick", "set_onfencedtreeclick", 0, 0, 0, 0, 0, 0, 1),
        ("onoverscroll", "get_onoverscroll", "set_onoverscroll", 0, 0, 0, 0, 0, 0, 1),
        ("onscrollend", "get_onscrollend", "set_onscrollend", 0, 0, 0, 0, 0, 0, 1),
        ("onscrollsnapchange", "get_onscrollsnapchange", "set_onscrollsnapchange", 0, 0, 0, 0, 0, 0, 1),
        ("onscrollsnapchanging", "get_onscrollsnapchanging", "set_onscrollsnapchanging", 0, 0, 0, 0, 0, 0, 1),
        ("onmove", "get_onmove", "set_onmove", 0, 0, 0, 0, 0, 0, 1),
        ("ontimezonechange", "get_ontimezonechange", "set_ontimezonechange", 0, 0, 0, 0, 0, 0, 1),
        ("crossOriginEmbedderPolicy", "get_crossOriginEmbedderPolicy", None, 0, 0, 0, 0, 0, 0, 1),
        ("translation", "get_translation", "set_translation", 0, 0, 0, 0, 0, 0, 1),
        ("fence", "get_fence", None, 0, 0, 0, 0, 0, 0, 1),
        ("testOriginTrialGlobalAttribute", "get_testOriginTrialGlobalAttribute", None, 0, 0, 0, 0, 0, 0, 1),
        ("caches", "get_caches", None, 0, 0, 0, 0, 0, 0, 1),
        ("cookieStore", "get_cookieStore", None, 0, 0, 0, 0, 0, 0, 1),
        ("ondevicemotion", "get_ondevicemotion", "set_ondevicemotion", 0, 0, 0, 0, 0, 0, 1),
        ("ondeviceorientation", "get_ondeviceorientation", "set_ondeviceorientation", 0, 0, 0, 0, 0, 0, 1),
        ("ondeviceorientationabsolute", "get_ondeviceorientationabsolute", "set_ondeviceorientationabsolute", 0, 0, 0, 0, 0, 0, 1),
        ("launchQueue", "get_launchQueue", None, 0, 0, 0, 0, 0, 0, 1),
        ("privateAttribution", "get_privateAttribution", "set_privateAttribution", 0, 0, 0, 0, 0, 0, 1),
        ("sharedStorage", "get_sharedStorage", None, 0, 0, 0, 0, 0, 0, 1),
        ("documentPictureInPicture", "get_documentPictureInPicture", None, 0, 0, 0, 0, 0, 0, 1),
        ("ontouchcancel", "get_ontouchcancel", "set_ontouchcancel", 0, 0, 0, 0, 0, 0, 1),
        ("ontouchend", "get_ontouchend", "set_ontouchend", 0, 0, 0, 0, 0, 0, 1),
        ("ontouchmove", "get_ontouchmove", "set_ontouchmove", 0, 0, 0, 0, 0, 0, 1),
        ("ontouchstart", "get_ontouchstart", "set_ontouchstart", 0, 0, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
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
        ("getComputedAccessibleNode", "fn_getComputedAccessibleNode", 1, 0, 0, 0, 1, 0, 0),
        ("webkitRequestFileSystem", "fn_webkitRequestFileSystem", 3, 0, 0, 0, 0, 0, 0),
        ("webkitResolveLocalFileSystemURL", "fn_webkitResolveLocalFileSystemURL", 2, 0, 0, 0, 0, 0, 0),
        ("fetchLater", "fn_fetchLater", 1, 0, 0, 0, 0, 0, 0),
        ("getDigitalGoodsService", "fn_getDigitalGoodsService", 1, 0, 0, 0, 1, 0, 0),
        ("getLockScreenData", "fn_getLockScreenData", 0, 0, 0, 0, 1, 0, 0),
        ("getScreenDetails", "fn_getScreenDetails", 0, 0, 0, 0, 1, 0, 0),
        ("maximize", "fn_maximize", 0, 0, 0, 0, 1, 0, 0),
        ("minimize", "fn_minimize", 0, 0, 0, 0, 1, 0, 0),
        ("restore", "fn_restore", 0, 0, 0, 0, 1, 0, 0),
        ("setResizable", "fn_setResizable", 1, 0, 0, 0, 1, 0, 0),
        ("openDatabase", "fn_openDatabase", 4, 0, 0, 0, 0, 0, 0),
        ("queryLocalFonts", "fn_queryLocalFonts", 0, 0, 0, 0, 1, 0, 0),
        ("showDirectoryPicker", "fn_showDirectoryPicker", 0, 0, 0, 0, 1, 0, 0),
        ("showOpenFilePicker", "fn_showOpenFilePicker", 0, 0, 0, 0, 1, 0, 0),
        ("showSaveFilePicker", "fn_showSaveFilePicker", 0, 0, 0, 0, 1, 0, 0),

    )

    def get_window(self):
        val = self._attr.get('window')
        if val is not None:
            return val
        logger.info(f'patch -> v8_window.py -> Window.window -> get attr')

    def get_self(self):
        val = self._attr.get('self')
        if val is not None:
            return val
        logger.info(f'patch -> v8_window.py -> Window.self -> get attr')

    def set_self(self, val):
        self._attr['self'] = val

    def get_document(self):
        val = self._attr.get('document')
        if val is not None:
            return val
        logger.info(f'patch -> v8_window.py -> Window.document -> get attr')

    def get_name(self):
        val = self._attr.get('name')
        if val is not None:
            return val
        logger.info(f'patch -> v8_window.py -> Window.name -> get attr')

    def set_name(self, val):
        self._attr['name'] = val

    def get_location(self):
        val = self._attr.get('location')
        if val is not None:
            return val
        logger.info(f'patch -> v8_window.py -> Window.location -> get attr')

    def set_location(self, val):
        self._attr['location'] = val

    def get_customElements(self):
        val = self._attr.get('customElements')
        if val is not None:
            return val
        logger.info(f'patch -> v8_window.py -> Window.customElements -> get attr')

    def get_history(self):
        val = self._attr.get('history')
        if val is not None:
            return val
        logger.info(f'patch -> v8_window.py -> Window.history -> get attr')

    def get_navigation(self):
        val = self._attr.get('navigation')
        if val is not None:
            return val
        logger.info(f'patch -> v8_window.py -> Window.navigation -> get attr')

    def set_navigation(self, val):
        self._attr['navigation'] = val

    def get_locationbar(self):
        val = self._attr.get('locationbar')
        if val is not None:
            return val
        logger.info(f'patch -> v8_window.py -> Window.locationbar -> get attr')

    def set_locationbar(self, val):
        self._attr['locationbar'] = val

    def get_menubar(self):
        val = self._attr.get('menubar')
        if val is not None:
            return val
        logger.info(f'patch -> v8_window.py -> Window.menubar -> get attr')

    def set_menubar(self, val):
        self._attr['menubar'] = val

    def get_personalbar(self):
        val = self._attr.get('personalbar')
        if val is not None:
            return val
        logger.info(f'patch -> v8_window.py -> Window.personalbar -> get attr')

    def set_personalbar(self, val):
        self._attr['personalbar'] = val

    def get_scrollbars(self):
        val = self._attr.get('scrollbars')
        if val is not None:
            return val
        logger.info(f'patch -> v8_window.py -> Window.scrollbars -> get attr')

    def set_scrollbars(self, val):
        self._attr['scrollbars'] = val

    def get_statusbar(self):
        val = self._attr.get('statusbar')
        if val is not None:
            return val
        logger.info(f'patch -> v8_window.py -> Window.statusbar -> get attr')

    def set_statusbar(self, val):
        self._attr['statusbar'] = val

    def get_toolbar(self):
        val = self._attr.get('toolbar')
        if val is not None:
            return val
        logger.info(f'patch -> v8_window.py -> Window.toolbar -> get attr')

    def set_toolbar(self, val):
        self._attr['toolbar'] = val

    def get_status(self):
        val = self._attr.get('status')
        if val is not None:
            return val
        logger.info(f'patch -> v8_window.py -> Window.status -> get attr')

    def set_status(self, val):
        self._attr['status'] = val

    def get_closed(self):
        val = self._attr.get('closed')
        if val is not None:
            return val
        logger.info(f'patch -> v8_window.py -> Window.closed -> get attr')

    def get_frames(self):
        val = self._attr.get('frames')
        if val is not None:
            return val
        logger.info(f'patch -> v8_window.py -> Window.frames -> get attr')

    def set_frames(self, val):
        self._attr['frames'] = val

    def get_length(self):
        val = self._attr.get('length')
        if val is not None:
            return val
        logger.info(f'patch -> v8_window.py -> Window.length -> get attr')

    def set_length(self, val):
        self._attr['length'] = val

    def get_top(self):
        val = self._attr.get('top')
        if val is not None:
            return val
        logger.info(f'patch -> v8_window.py -> Window.top -> get attr')

    def get_opener(self):
        val = self._attr.get('opener')
        if val is not None:
            return val
        logger.info(f'patch -> v8_window.py -> Window.opener -> get attr')

    def set_opener(self, val):
        self._attr['opener'] = val

    def get_parent(self):
        val = self._attr.get('parent')
        if val is not None:
            return val
        logger.info(f'patch -> v8_window.py -> Window.parent -> get attr')

    def set_parent(self, val):
        self._attr['parent'] = val

    def get_frameElement(self):
        val = self._attr.get('frameElement')
        if val is not None:
            return val
        logger.info(f'patch -> v8_window.py -> Window.frameElement -> get attr')

    def get_navigator(self):
        val = self._attr.get('navigator')
        if val is not None:
            return val
        logger.info(f'patch -> v8_window.py -> Window.navigator -> get attr')

    def get_origin(self):
        val = self._attr.get('origin')
        if val is not None:
            return val
        logger.info(f'patch -> v8_window.py -> Window.origin -> get attr')

    def set_origin(self, val):
        self._attr['origin'] = val

    def get_external(self):
        val = self._attr.get('external')
        if val is not None:
            return val
        logger.info(f'patch -> v8_window.py -> Window.external -> get attr')

    def set_external(self, val):
        self._attr['external'] = val

    def get_screen(self):
        val = self._attr.get('screen')
        if val is not None:
            return val
        logger.info(f'patch -> v8_window.py -> Window.screen -> get attr')

    def set_screen(self, val):
        self._attr['screen'] = val

    def get_innerWidth(self):
        val = self._attr.get('innerWidth')
        if val is not None:
            return val
        logger.info(f'patch -> v8_window.py -> Window.innerWidth -> get attr')

    def set_innerWidth(self, val):
        self._attr['innerWidth'] = val

    def get_innerHeight(self):
        val = self._attr.get('innerHeight')
        if val is not None:
            return val
        logger.info(f'patch -> v8_window.py -> Window.innerHeight -> get attr')

    def set_innerHeight(self, val):
        self._attr['innerHeight'] = val

    def get_scrollX(self):
        val = self._attr.get('scrollX')
        if val is not None:
            return val
        logger.info(f'patch -> v8_window.py -> Window.scrollX -> get attr')

    def set_scrollX(self, val):
        self._attr['scrollX'] = val

    def get_pageXOffset(self):
        val = self._attr.get('pageXOffset')
        if val is not None:
            return val
        logger.info(f'patch -> v8_window.py -> Window.pageXOffset -> get attr')

    def set_pageXOffset(self, val):
        self._attr['pageXOffset'] = val

    def get_scrollY(self):
        val = self._attr.get('scrollY')
        if val is not None:
            return val
        logger.info(f'patch -> v8_window.py -> Window.scrollY -> get attr')

    def set_scrollY(self, val):
        self._attr['scrollY'] = val

    def get_pageYOffset(self):
        val = self._attr.get('pageYOffset')
        if val is not None:
            return val
        logger.info(f'patch -> v8_window.py -> Window.pageYOffset -> get attr')

    def set_pageYOffset(self, val):
        self._attr['pageYOffset'] = val

    def get_visualViewport(self):
        val = self._attr.get('visualViewport')
        if val is not None:
            return val
        logger.info(f'patch -> v8_window.py -> Window.visualViewport -> get attr')

    def set_visualViewport(self, val):
        self._attr['visualViewport'] = val

    def get_screenX(self):
        val = self._attr.get('screenX')
        if val is not None:
            return val
        logger.info(f'patch -> v8_window.py -> Window.screenX -> get attr')

    def set_screenX(self, val):
        self._attr['screenX'] = val

    def get_screenY(self):
        val = self._attr.get('screenY')
        if val is not None:
            return val
        logger.info(f'patch -> v8_window.py -> Window.screenY -> get attr')

    def set_screenY(self, val):
        self._attr['screenY'] = val

    def get_outerWidth(self):
        val = self._attr.get('outerWidth')
        if val is not None:
            return val
        logger.info(f'patch -> v8_window.py -> Window.outerWidth -> get attr')

    def set_outerWidth(self, val):
        self._attr['outerWidth'] = val

    def get_outerHeight(self):
        val = self._attr.get('outerHeight')
        if val is not None:
            return val
        logger.info(f'patch -> v8_window.py -> Window.outerHeight -> get attr')

    def set_outerHeight(self, val):
        self._attr['outerHeight'] = val

    def get_devicePixelRatio(self):
        val = self._attr.get('devicePixelRatio')
        if val is not None:
            return val
        logger.info(f'patch -> v8_window.py -> Window.devicePixelRatio -> get attr')

    def set_devicePixelRatio(self, val):
        self._attr['devicePixelRatio'] = val

    def get_event(self):
        val = self._attr.get('event')
        if val is not None:
            return val
        logger.info(f'patch -> v8_window.py -> Window.event -> get attr')

    def set_event(self, val):
        self._attr['event'] = val

    def get_clientInformation(self):
        val = self._attr.get('clientInformation')
        if val is not None:
            return val
        logger.info(f'patch -> v8_window.py -> Window.clientInformation -> get attr')

    def set_clientInformation(self, val):
        self._attr['clientInformation'] = val

    def get_offscreenBuffering(self):
        val = self._attr.get('offscreenBuffering')
        if val is not None:
            return val
        logger.info(f'patch -> v8_window.py -> Window.offscreenBuffering -> get attr')

    def set_offscreenBuffering(self, val):
        self._attr['offscreenBuffering'] = val

    def get_screenLeft(self):
        val = self._attr.get('screenLeft')
        if val is not None:
            return val
        logger.info(f'patch -> v8_window.py -> Window.screenLeft -> get attr')

    def set_screenLeft(self, val):
        self._attr['screenLeft'] = val

    def get_screenTop(self):
        val = self._attr.get('screenTop')
        if val is not None:
            return val
        logger.info(f'patch -> v8_window.py -> Window.screenTop -> get attr')

    def set_screenTop(self, val):
        self._attr['screenTop'] = val

    def get_styleMedia(self):
        val = self._attr.get('styleMedia')
        if val is not None:
            return val
        logger.info(f'patch -> v8_window.py -> Window.styleMedia -> get attr')

    def get_onsearch(self):
        val = self._attr.get('onsearch')
        if val is not None:
            return val
        logger.info(f'patch -> v8_window.py -> Window.onsearch -> get attr')

    def set_onsearch(self, val):
        self._attr['onsearch'] = val

    def get_isSecureContext(self):
        val = self._attr.get('isSecureContext')
        if val is not None:
            return val
        logger.info(f'patch -> v8_window.py -> Window.isSecureContext -> get attr')

    def get_trustedTypes(self):
        val = self._attr.get('trustedTypes')
        if val is not None:
            return val
        logger.info(f'patch -> v8_window.py -> Window.trustedTypes -> get attr')

    def get_performance(self):
        val = self._attr.get('performance')
        if val is not None:
            return val
        logger.info(f'patch -> v8_window.py -> Window.performance -> get attr')

    def set_performance(self, val):
        self._attr['performance'] = val

    def get_onappinstalled(self):
        val = self._attr.get('onappinstalled')
        if val is not None:
            return val
        logger.info(f'patch -> v8_window.py -> Window.onappinstalled -> get attr')

    def set_onappinstalled(self, val):
        self._attr['onappinstalled'] = val

    def get_onbeforeinstallprompt(self):
        val = self._attr.get('onbeforeinstallprompt')
        if val is not None:
            return val
        logger.info(f'patch -> v8_window.py -> Window.onbeforeinstallprompt -> get attr')

    def set_onbeforeinstallprompt(self, val):
        self._attr['onbeforeinstallprompt'] = val

    def get_crypto(self):
        val = self._attr.get('crypto')
        if val is not None:
            return val
        logger.info(f'patch -> v8_window.py -> Window.crypto -> get attr')

    def get_indexedDB(self):
        val = self._attr.get('indexedDB')
        if val is not None:
            return val
        logger.info(f'patch -> v8_window.py -> Window.indexedDB -> get attr')

    def get_sessionStorage(self):
        val = self._attr.get('sessionStorage')
        if val is not None:
            return val
        logger.info(f'patch -> v8_window.py -> Window.sessionStorage -> get attr')

    def get_localStorage(self):
        val = self._attr.get('localStorage')
        if val is not None:
            return val
        logger.info(f'patch -> v8_window.py -> Window.localStorage -> get attr')

    def get_onbeforexrselect(self):
        val = self._attr.get('onbeforexrselect')
        if val is not None:
            return val
        logger.info(f'patch -> v8_window.py -> Window.onbeforexrselect -> get attr')

    def set_onbeforexrselect(self, val):
        self._attr['onbeforexrselect'] = val

    def get_onabort(self):
        val = self._attr.get('onabort')
        if val is not None:
            return val
        logger.info(f'patch -> v8_window.py -> Window.onabort -> get attr')

    def set_onabort(self, val):
        self._attr['onabort'] = val

    def get_onbeforeinput(self):
        val = self._attr.get('onbeforeinput')
        if val is not None:
            return val
        logger.info(f'patch -> v8_window.py -> Window.onbeforeinput -> get attr')

    def set_onbeforeinput(self, val):
        self._attr['onbeforeinput'] = val

    def get_onbeforematch(self):
        val = self._attr.get('onbeforematch')
        if val is not None:
            return val
        logger.info(f'patch -> v8_window.py -> Window.onbeforematch -> get attr')

    def set_onbeforematch(self, val):
        self._attr['onbeforematch'] = val

    def get_onbeforetoggle(self):
        val = self._attr.get('onbeforetoggle')
        if val is not None:
            return val
        logger.info(f'patch -> v8_window.py -> Window.onbeforetoggle -> get attr')

    def set_onbeforetoggle(self, val):
        self._attr['onbeforetoggle'] = val

    def get_onblur(self):
        val = self._attr.get('onblur')
        if val is not None:
            return val
        logger.info(f'patch -> v8_window.py -> Window.onblur -> get attr')

    def set_onblur(self, val):
        self._attr['onblur'] = val

    def get_oncancel(self):
        val = self._attr.get('oncancel')
        if val is not None:
            return val
        logger.info(f'patch -> v8_window.py -> Window.oncancel -> get attr')

    def set_oncancel(self, val):
        self._attr['oncancel'] = val

    def get_oncanplay(self):
        val = self._attr.get('oncanplay')
        if val is not None:
            return val
        logger.info(f'patch -> v8_window.py -> Window.oncanplay -> get attr')

    def set_oncanplay(self, val):
        self._attr['oncanplay'] = val

    def get_oncanplaythrough(self):
        val = self._attr.get('oncanplaythrough')
        if val is not None:
            return val
        logger.info(f'patch -> v8_window.py -> Window.oncanplaythrough -> get attr')

    def set_oncanplaythrough(self, val):
        self._attr['oncanplaythrough'] = val

    def get_onchange(self):
        val = self._attr.get('onchange')
        if val is not None:
            return val
        logger.info(f'patch -> v8_window.py -> Window.onchange -> get attr')

    def set_onchange(self, val):
        self._attr['onchange'] = val

    def get_onclick(self):
        val = self._attr.get('onclick')
        if val is not None:
            return val
        logger.info(f'patch -> v8_window.py -> Window.onclick -> get attr')

    def set_onclick(self, val):
        self._attr['onclick'] = val

    def get_onclose(self):
        val = self._attr.get('onclose')
        if val is not None:
            return val
        logger.info(f'patch -> v8_window.py -> Window.onclose -> get attr')

    def set_onclose(self, val):
        self._attr['onclose'] = val

    def get_oncontentvisibilityautostatechange(self):
        val = self._attr.get('oncontentvisibilityautostatechange')
        if val is not None:
            return val
        logger.info(f'patch -> v8_window.py -> Window.oncontentvisibilityautostatechange -> get attr')

    def set_oncontentvisibilityautostatechange(self, val):
        self._attr['oncontentvisibilityautostatechange'] = val

    def get_oncontextlost(self):
        val = self._attr.get('oncontextlost')
        if val is not None:
            return val
        logger.info(f'patch -> v8_window.py -> Window.oncontextlost -> get attr')

    def set_oncontextlost(self, val):
        self._attr['oncontextlost'] = val

    def get_oncontextmenu(self):
        val = self._attr.get('oncontextmenu')
        if val is not None:
            return val
        logger.info(f'patch -> v8_window.py -> Window.oncontextmenu -> get attr')

    def set_oncontextmenu(self, val):
        self._attr['oncontextmenu'] = val

    def get_oncontextrestored(self):
        val = self._attr.get('oncontextrestored')
        if val is not None:
            return val
        logger.info(f'patch -> v8_window.py -> Window.oncontextrestored -> get attr')

    def set_oncontextrestored(self, val):
        self._attr['oncontextrestored'] = val

    def get_oncuechange(self):
        val = self._attr.get('oncuechange')
        if val is not None:
            return val
        logger.info(f'patch -> v8_window.py -> Window.oncuechange -> get attr')

    def set_oncuechange(self, val):
        self._attr['oncuechange'] = val

    def get_ondblclick(self):
        val = self._attr.get('ondblclick')
        if val is not None:
            return val
        logger.info(f'patch -> v8_window.py -> Window.ondblclick -> get attr')

    def set_ondblclick(self, val):
        self._attr['ondblclick'] = val

    def get_ondrag(self):
        val = self._attr.get('ondrag')
        if val is not None:
            return val
        logger.info(f'patch -> v8_window.py -> Window.ondrag -> get attr')

    def set_ondrag(self, val):
        self._attr['ondrag'] = val

    def get_ondragend(self):
        val = self._attr.get('ondragend')
        if val is not None:
            return val
        logger.info(f'patch -> v8_window.py -> Window.ondragend -> get attr')

    def set_ondragend(self, val):
        self._attr['ondragend'] = val

    def get_ondragenter(self):
        val = self._attr.get('ondragenter')
        if val is not None:
            return val
        logger.info(f'patch -> v8_window.py -> Window.ondragenter -> get attr')

    def set_ondragenter(self, val):
        self._attr['ondragenter'] = val

    def get_ondragleave(self):
        val = self._attr.get('ondragleave')
        if val is not None:
            return val
        logger.info(f'patch -> v8_window.py -> Window.ondragleave -> get attr')

    def set_ondragleave(self, val):
        self._attr['ondragleave'] = val

    def get_ondragover(self):
        val = self._attr.get('ondragover')
        if val is not None:
            return val
        logger.info(f'patch -> v8_window.py -> Window.ondragover -> get attr')

    def set_ondragover(self, val):
        self._attr['ondragover'] = val

    def get_ondragstart(self):
        val = self._attr.get('ondragstart')
        if val is not None:
            return val
        logger.info(f'patch -> v8_window.py -> Window.ondragstart -> get attr')

    def set_ondragstart(self, val):
        self._attr['ondragstart'] = val

    def get_ondrop(self):
        val = self._attr.get('ondrop')
        if val is not None:
            return val
        logger.info(f'patch -> v8_window.py -> Window.ondrop -> get attr')

    def set_ondrop(self, val):
        self._attr['ondrop'] = val

    def get_ondurationchange(self):
        val = self._attr.get('ondurationchange')
        if val is not None:
            return val
        logger.info(f'patch -> v8_window.py -> Window.ondurationchange -> get attr')

    def set_ondurationchange(self, val):
        self._attr['ondurationchange'] = val

    def get_onemptied(self):
        val = self._attr.get('onemptied')
        if val is not None:
            return val
        logger.info(f'patch -> v8_window.py -> Window.onemptied -> get attr')

    def set_onemptied(self, val):
        self._attr['onemptied'] = val

    def get_onended(self):
        val = self._attr.get('onended')
        if val is not None:
            return val
        logger.info(f'patch -> v8_window.py -> Window.onended -> get attr')

    def set_onended(self, val):
        self._attr['onended'] = val

    def get_onerror(self):
        val = self._attr.get('onerror')
        if val is not None:
            return val
        logger.info(f'patch -> v8_window.py -> Window.onerror -> get attr')

    def set_onerror(self, val):
        self._attr['onerror'] = val

    def get_onfocus(self):
        val = self._attr.get('onfocus')
        if val is not None:
            return val
        logger.info(f'patch -> v8_window.py -> Window.onfocus -> get attr')

    def set_onfocus(self, val):
        self._attr['onfocus'] = val

    def get_onformdata(self):
        val = self._attr.get('onformdata')
        if val is not None:
            return val
        logger.info(f'patch -> v8_window.py -> Window.onformdata -> get attr')

    def set_onformdata(self, val):
        self._attr['onformdata'] = val

    def get_oninput(self):
        val = self._attr.get('oninput')
        if val is not None:
            return val
        logger.info(f'patch -> v8_window.py -> Window.oninput -> get attr')

    def set_oninput(self, val):
        self._attr['oninput'] = val

    def get_oninvalid(self):
        val = self._attr.get('oninvalid')
        if val is not None:
            return val
        logger.info(f'patch -> v8_window.py -> Window.oninvalid -> get attr')

    def set_oninvalid(self, val):
        self._attr['oninvalid'] = val

    def get_onkeydown(self):
        val = self._attr.get('onkeydown')
        if val is not None:
            return val
        logger.info(f'patch -> v8_window.py -> Window.onkeydown -> get attr')

    def set_onkeydown(self, val):
        self._attr['onkeydown'] = val

    def get_onkeypress(self):
        val = self._attr.get('onkeypress')
        if val is not None:
            return val
        logger.info(f'patch -> v8_window.py -> Window.onkeypress -> get attr')

    def set_onkeypress(self, val):
        self._attr['onkeypress'] = val

    def get_onkeyup(self):
        val = self._attr.get('onkeyup')
        if val is not None:
            return val
        logger.info(f'patch -> v8_window.py -> Window.onkeyup -> get attr')

    def set_onkeyup(self, val):
        self._attr['onkeyup'] = val

    def get_onload(self):
        val = self._attr.get('onload')
        if val is not None:
            return val
        logger.info(f'patch -> v8_window.py -> Window.onload -> get attr')

    def set_onload(self, val):
        self._attr['onload'] = val

    def get_onloadeddata(self):
        val = self._attr.get('onloadeddata')
        if val is not None:
            return val
        logger.info(f'patch -> v8_window.py -> Window.onloadeddata -> get attr')

    def set_onloadeddata(self, val):
        self._attr['onloadeddata'] = val

    def get_onloadedmetadata(self):
        val = self._attr.get('onloadedmetadata')
        if val is not None:
            return val
        logger.info(f'patch -> v8_window.py -> Window.onloadedmetadata -> get attr')

    def set_onloadedmetadata(self, val):
        self._attr['onloadedmetadata'] = val

    def get_onloadstart(self):
        val = self._attr.get('onloadstart')
        if val is not None:
            return val
        logger.info(f'patch -> v8_window.py -> Window.onloadstart -> get attr')

    def set_onloadstart(self, val):
        self._attr['onloadstart'] = val

    def get_onmousedown(self):
        val = self._attr.get('onmousedown')
        if val is not None:
            return val
        logger.info(f'patch -> v8_window.py -> Window.onmousedown -> get attr')

    def set_onmousedown(self, val):
        self._attr['onmousedown'] = val

    def get_onmouseenter(self):
        val = self._attr.get('onmouseenter')
        if val is not None:
            return val
        logger.info(f'patch -> v8_window.py -> Window.onmouseenter -> get attr')

    def set_onmouseenter(self, val):
        self._attr['onmouseenter'] = val

    def get_onmouseleave(self):
        val = self._attr.get('onmouseleave')
        if val is not None:
            return val
        logger.info(f'patch -> v8_window.py -> Window.onmouseleave -> get attr')

    def set_onmouseleave(self, val):
        self._attr['onmouseleave'] = val

    def get_onmousemove(self):
        val = self._attr.get('onmousemove')
        if val is not None:
            return val
        logger.info(f'patch -> v8_window.py -> Window.onmousemove -> get attr')

    def set_onmousemove(self, val):
        self._attr['onmousemove'] = val

    def get_onmouseout(self):
        val = self._attr.get('onmouseout')
        if val is not None:
            return val
        logger.info(f'patch -> v8_window.py -> Window.onmouseout -> get attr')

    def set_onmouseout(self, val):
        self._attr['onmouseout'] = val

    def get_onmouseover(self):
        val = self._attr.get('onmouseover')
        if val is not None:
            return val
        logger.info(f'patch -> v8_window.py -> Window.onmouseover -> get attr')

    def set_onmouseover(self, val):
        self._attr['onmouseover'] = val

    def get_onmouseup(self):
        val = self._attr.get('onmouseup')
        if val is not None:
            return val
        logger.info(f'patch -> v8_window.py -> Window.onmouseup -> get attr')

    def set_onmouseup(self, val):
        self._attr['onmouseup'] = val

    def get_onmousewheel(self):
        val = self._attr.get('onmousewheel')
        if val is not None:
            return val
        logger.info(f'patch -> v8_window.py -> Window.onmousewheel -> get attr')

    def set_onmousewheel(self, val):
        self._attr['onmousewheel'] = val

    def get_onpause(self):
        val = self._attr.get('onpause')
        if val is not None:
            return val
        logger.info(f'patch -> v8_window.py -> Window.onpause -> get attr')

    def set_onpause(self, val):
        self._attr['onpause'] = val

    def get_onplay(self):
        val = self._attr.get('onplay')
        if val is not None:
            return val
        logger.info(f'patch -> v8_window.py -> Window.onplay -> get attr')

    def set_onplay(self, val):
        self._attr['onplay'] = val

    def get_onplaying(self):
        val = self._attr.get('onplaying')
        if val is not None:
            return val
        logger.info(f'patch -> v8_window.py -> Window.onplaying -> get attr')

    def set_onplaying(self, val):
        self._attr['onplaying'] = val

    def get_onprogress(self):
        val = self._attr.get('onprogress')
        if val is not None:
            return val
        logger.info(f'patch -> v8_window.py -> Window.onprogress -> get attr')

    def set_onprogress(self, val):
        self._attr['onprogress'] = val

    def get_onratechange(self):
        val = self._attr.get('onratechange')
        if val is not None:
            return val
        logger.info(f'patch -> v8_window.py -> Window.onratechange -> get attr')

    def set_onratechange(self, val):
        self._attr['onratechange'] = val

    def get_onreset(self):
        val = self._attr.get('onreset')
        if val is not None:
            return val
        logger.info(f'patch -> v8_window.py -> Window.onreset -> get attr')

    def set_onreset(self, val):
        self._attr['onreset'] = val

    def get_onresize(self):
        val = self._attr.get('onresize')
        if val is not None:
            return val
        logger.info(f'patch -> v8_window.py -> Window.onresize -> get attr')

    def set_onresize(self, val):
        self._attr['onresize'] = val

    def get_onscroll(self):
        val = self._attr.get('onscroll')
        if val is not None:
            return val
        logger.info(f'patch -> v8_window.py -> Window.onscroll -> get attr')

    def set_onscroll(self, val):
        self._attr['onscroll'] = val

    def get_onsecuritypolicyviolation(self):
        val = self._attr.get('onsecuritypolicyviolation')
        if val is not None:
            return val
        logger.info(f'patch -> v8_window.py -> Window.onsecuritypolicyviolation -> get attr')

    def set_onsecuritypolicyviolation(self, val):
        self._attr['onsecuritypolicyviolation'] = val

    def get_onseeked(self):
        val = self._attr.get('onseeked')
        if val is not None:
            return val
        logger.info(f'patch -> v8_window.py -> Window.onseeked -> get attr')

    def set_onseeked(self, val):
        self._attr['onseeked'] = val

    def get_onseeking(self):
        val = self._attr.get('onseeking')
        if val is not None:
            return val
        logger.info(f'patch -> v8_window.py -> Window.onseeking -> get attr')

    def set_onseeking(self, val):
        self._attr['onseeking'] = val

    def get_onselect(self):
        val = self._attr.get('onselect')
        if val is not None:
            return val
        logger.info(f'patch -> v8_window.py -> Window.onselect -> get attr')

    def set_onselect(self, val):
        self._attr['onselect'] = val

    def get_onslotchange(self):
        val = self._attr.get('onslotchange')
        if val is not None:
            return val
        logger.info(f'patch -> v8_window.py -> Window.onslotchange -> get attr')

    def set_onslotchange(self, val):
        self._attr['onslotchange'] = val

    def get_onstalled(self):
        val = self._attr.get('onstalled')
        if val is not None:
            return val
        logger.info(f'patch -> v8_window.py -> Window.onstalled -> get attr')

    def set_onstalled(self, val):
        self._attr['onstalled'] = val

    def get_onsubmit(self):
        val = self._attr.get('onsubmit')
        if val is not None:
            return val
        logger.info(f'patch -> v8_window.py -> Window.onsubmit -> get attr')

    def set_onsubmit(self, val):
        self._attr['onsubmit'] = val

    def get_onsuspend(self):
        val = self._attr.get('onsuspend')
        if val is not None:
            return val
        logger.info(f'patch -> v8_window.py -> Window.onsuspend -> get attr')

    def set_onsuspend(self, val):
        self._attr['onsuspend'] = val

    def get_ontimeupdate(self):
        val = self._attr.get('ontimeupdate')
        if val is not None:
            return val
        logger.info(f'patch -> v8_window.py -> Window.ontimeupdate -> get attr')

    def set_ontimeupdate(self, val):
        self._attr['ontimeupdate'] = val

    def get_ontoggle(self):
        val = self._attr.get('ontoggle')
        if val is not None:
            return val
        logger.info(f'patch -> v8_window.py -> Window.ontoggle -> get attr')

    def set_ontoggle(self, val):
        self._attr['ontoggle'] = val

    def get_onvolumechange(self):
        val = self._attr.get('onvolumechange')
        if val is not None:
            return val
        logger.info(f'patch -> v8_window.py -> Window.onvolumechange -> get attr')

    def set_onvolumechange(self, val):
        self._attr['onvolumechange'] = val

    def get_onwaiting(self):
        val = self._attr.get('onwaiting')
        if val is not None:
            return val
        logger.info(f'patch -> v8_window.py -> Window.onwaiting -> get attr')

    def set_onwaiting(self, val):
        self._attr['onwaiting'] = val

    def get_onwebkitanimationend(self):
        val = self._attr.get('onwebkitanimationend')
        if val is not None:
            return val
        logger.info(f'patch -> v8_window.py -> Window.onwebkitanimationend -> get attr')

    def set_onwebkitanimationend(self, val):
        self._attr['onwebkitanimationend'] = val

    def get_onwebkitanimationiteration(self):
        val = self._attr.get('onwebkitanimationiteration')
        if val is not None:
            return val
        logger.info(f'patch -> v8_window.py -> Window.onwebkitanimationiteration -> get attr')

    def set_onwebkitanimationiteration(self, val):
        self._attr['onwebkitanimationiteration'] = val

    def get_onwebkitanimationstart(self):
        val = self._attr.get('onwebkitanimationstart')
        if val is not None:
            return val
        logger.info(f'patch -> v8_window.py -> Window.onwebkitanimationstart -> get attr')

    def set_onwebkitanimationstart(self, val):
        self._attr['onwebkitanimationstart'] = val

    def get_onwebkittransitionend(self):
        val = self._attr.get('onwebkittransitionend')
        if val is not None:
            return val
        logger.info(f'patch -> v8_window.py -> Window.onwebkittransitionend -> get attr')

    def set_onwebkittransitionend(self, val):
        self._attr['onwebkittransitionend'] = val

    def get_onwheel(self):
        val = self._attr.get('onwheel')
        if val is not None:
            return val
        logger.info(f'patch -> v8_window.py -> Window.onwheel -> get attr')

    def set_onwheel(self, val):
        self._attr['onwheel'] = val

    def get_onauxclick(self):
        val = self._attr.get('onauxclick')
        if val is not None:
            return val
        logger.info(f'patch -> v8_window.py -> Window.onauxclick -> get attr')

    def set_onauxclick(self, val):
        self._attr['onauxclick'] = val

    def get_ongotpointercapture(self):
        val = self._attr.get('ongotpointercapture')
        if val is not None:
            return val
        logger.info(f'patch -> v8_window.py -> Window.ongotpointercapture -> get attr')

    def set_ongotpointercapture(self, val):
        self._attr['ongotpointercapture'] = val

    def get_onlostpointercapture(self):
        val = self._attr.get('onlostpointercapture')
        if val is not None:
            return val
        logger.info(f'patch -> v8_window.py -> Window.onlostpointercapture -> get attr')

    def set_onlostpointercapture(self, val):
        self._attr['onlostpointercapture'] = val

    def get_onpointerdown(self):
        val = self._attr.get('onpointerdown')
        if val is not None:
            return val
        logger.info(f'patch -> v8_window.py -> Window.onpointerdown -> get attr')

    def set_onpointerdown(self, val):
        self._attr['onpointerdown'] = val

    def get_onpointermove(self):
        val = self._attr.get('onpointermove')
        if val is not None:
            return val
        logger.info(f'patch -> v8_window.py -> Window.onpointermove -> get attr')

    def set_onpointermove(self, val):
        self._attr['onpointermove'] = val

    def get_onpointerrawupdate(self):
        val = self._attr.get('onpointerrawupdate')
        if val is not None:
            return val
        logger.info(f'patch -> v8_window.py -> Window.onpointerrawupdate -> get attr')

    def set_onpointerrawupdate(self, val):
        self._attr['onpointerrawupdate'] = val

    def get_onpointerup(self):
        val = self._attr.get('onpointerup')
        if val is not None:
            return val
        logger.info(f'patch -> v8_window.py -> Window.onpointerup -> get attr')

    def set_onpointerup(self, val):
        self._attr['onpointerup'] = val

    def get_onpointercancel(self):
        val = self._attr.get('onpointercancel')
        if val is not None:
            return val
        logger.info(f'patch -> v8_window.py -> Window.onpointercancel -> get attr')

    def set_onpointercancel(self, val):
        self._attr['onpointercancel'] = val

    def get_onpointerover(self):
        val = self._attr.get('onpointerover')
        if val is not None:
            return val
        logger.info(f'patch -> v8_window.py -> Window.onpointerover -> get attr')

    def set_onpointerover(self, val):
        self._attr['onpointerover'] = val

    def get_onpointerout(self):
        val = self._attr.get('onpointerout')
        if val is not None:
            return val
        logger.info(f'patch -> v8_window.py -> Window.onpointerout -> get attr')

    def set_onpointerout(self, val):
        self._attr['onpointerout'] = val

    def get_onpointerenter(self):
        val = self._attr.get('onpointerenter')
        if val is not None:
            return val
        logger.info(f'patch -> v8_window.py -> Window.onpointerenter -> get attr')

    def set_onpointerenter(self, val):
        self._attr['onpointerenter'] = val

    def get_onpointerleave(self):
        val = self._attr.get('onpointerleave')
        if val is not None:
            return val
        logger.info(f'patch -> v8_window.py -> Window.onpointerleave -> get attr')

    def set_onpointerleave(self, val):
        self._attr['onpointerleave'] = val

    def get_onselectstart(self):
        val = self._attr.get('onselectstart')
        if val is not None:
            return val
        logger.info(f'patch -> v8_window.py -> Window.onselectstart -> get attr')

    def set_onselectstart(self, val):
        self._attr['onselectstart'] = val

    def get_onselectionchange(self):
        val = self._attr.get('onselectionchange')
        if val is not None:
            return val
        logger.info(f'patch -> v8_window.py -> Window.onselectionchange -> get attr')

    def set_onselectionchange(self, val):
        self._attr['onselectionchange'] = val

    def get_onanimationend(self):
        val = self._attr.get('onanimationend')
        if val is not None:
            return val
        logger.info(f'patch -> v8_window.py -> Window.onanimationend -> get attr')

    def set_onanimationend(self, val):
        self._attr['onanimationend'] = val

    def get_onanimationiteration(self):
        val = self._attr.get('onanimationiteration')
        if val is not None:
            return val
        logger.info(f'patch -> v8_window.py -> Window.onanimationiteration -> get attr')

    def set_onanimationiteration(self, val):
        self._attr['onanimationiteration'] = val

    def get_onanimationstart(self):
        val = self._attr.get('onanimationstart')
        if val is not None:
            return val
        logger.info(f'patch -> v8_window.py -> Window.onanimationstart -> get attr')

    def set_onanimationstart(self, val):
        self._attr['onanimationstart'] = val

    def get_ontransitionrun(self):
        val = self._attr.get('ontransitionrun')
        if val is not None:
            return val
        logger.info(f'patch -> v8_window.py -> Window.ontransitionrun -> get attr')

    def set_ontransitionrun(self, val):
        self._attr['ontransitionrun'] = val

    def get_ontransitionstart(self):
        val = self._attr.get('ontransitionstart')
        if val is not None:
            return val
        logger.info(f'patch -> v8_window.py -> Window.ontransitionstart -> get attr')

    def set_ontransitionstart(self, val):
        self._attr['ontransitionstart'] = val

    def get_ontransitionend(self):
        val = self._attr.get('ontransitionend')
        if val is not None:
            return val
        logger.info(f'patch -> v8_window.py -> Window.ontransitionend -> get attr')

    def set_ontransitionend(self, val):
        self._attr['ontransitionend'] = val

    def get_ontransitioncancel(self):
        val = self._attr.get('ontransitioncancel')
        if val is not None:
            return val
        logger.info(f'patch -> v8_window.py -> Window.ontransitioncancel -> get attr')

    def set_ontransitioncancel(self, val):
        self._attr['ontransitioncancel'] = val

    def get_onafterprint(self):
        val = self._attr.get('onafterprint')
        if val is not None:
            return val
        logger.info(f'patch -> v8_window.py -> Window.onafterprint -> get attr')

    def set_onafterprint(self, val):
        self._attr['onafterprint'] = val

    def get_onbeforeprint(self):
        val = self._attr.get('onbeforeprint')
        if val is not None:
            return val
        logger.info(f'patch -> v8_window.py -> Window.onbeforeprint -> get attr')

    def set_onbeforeprint(self, val):
        self._attr['onbeforeprint'] = val

    def get_onbeforeunload(self):
        val = self._attr.get('onbeforeunload')
        if val is not None:
            return val
        logger.info(f'patch -> v8_window.py -> Window.onbeforeunload -> get attr')

    def set_onbeforeunload(self, val):
        self._attr['onbeforeunload'] = val

    def get_onhashchange(self):
        val = self._attr.get('onhashchange')
        if val is not None:
            return val
        logger.info(f'patch -> v8_window.py -> Window.onhashchange -> get attr')

    def set_onhashchange(self, val):
        self._attr['onhashchange'] = val

    def get_onlanguagechange(self):
        val = self._attr.get('onlanguagechange')
        if val is not None:
            return val
        logger.info(f'patch -> v8_window.py -> Window.onlanguagechange -> get attr')

    def set_onlanguagechange(self, val):
        self._attr['onlanguagechange'] = val

    def get_onmessage(self):
        val = self._attr.get('onmessage')
        if val is not None:
            return val
        logger.info(f'patch -> v8_window.py -> Window.onmessage -> get attr')

    def set_onmessage(self, val):
        self._attr['onmessage'] = val

    def get_onmessageerror(self):
        val = self._attr.get('onmessageerror')
        if val is not None:
            return val
        logger.info(f'patch -> v8_window.py -> Window.onmessageerror -> get attr')

    def set_onmessageerror(self, val):
        self._attr['onmessageerror'] = val

    def get_onoffline(self):
        val = self._attr.get('onoffline')
        if val is not None:
            return val
        logger.info(f'patch -> v8_window.py -> Window.onoffline -> get attr')

    def set_onoffline(self, val):
        self._attr['onoffline'] = val

    def get_ononline(self):
        val = self._attr.get('ononline')
        if val is not None:
            return val
        logger.info(f'patch -> v8_window.py -> Window.ononline -> get attr')

    def set_ononline(self, val):
        self._attr['ononline'] = val

    def get_onpagehide(self):
        val = self._attr.get('onpagehide')
        if val is not None:
            return val
        logger.info(f'patch -> v8_window.py -> Window.onpagehide -> get attr')

    def set_onpagehide(self, val):
        self._attr['onpagehide'] = val

    def get_onpageshow(self):
        val = self._attr.get('onpageshow')
        if val is not None:
            return val
        logger.info(f'patch -> v8_window.py -> Window.onpageshow -> get attr')

    def set_onpageshow(self, val):
        self._attr['onpageshow'] = val

    def get_onpopstate(self):
        val = self._attr.get('onpopstate')
        if val is not None:
            return val
        logger.info(f'patch -> v8_window.py -> Window.onpopstate -> get attr')

    def set_onpopstate(self, val):
        self._attr['onpopstate'] = val

    def get_onrejectionhandled(self):
        val = self._attr.get('onrejectionhandled')
        if val is not None:
            return val
        logger.info(f'patch -> v8_window.py -> Window.onrejectionhandled -> get attr')

    def set_onrejectionhandled(self, val):
        self._attr['onrejectionhandled'] = val

    def get_onstorage(self):
        val = self._attr.get('onstorage')
        if val is not None:
            return val
        logger.info(f'patch -> v8_window.py -> Window.onstorage -> get attr')

    def set_onstorage(self, val):
        self._attr['onstorage'] = val

    def get_onunhandledrejection(self):
        val = self._attr.get('onunhandledrejection')
        if val is not None:
            return val
        logger.info(f'patch -> v8_window.py -> Window.onunhandledrejection -> get attr')

    def set_onunhandledrejection(self, val):
        self._attr['onunhandledrejection'] = val

    def get_onunload(self):
        val = self._attr.get('onunload')
        if val is not None:
            return val
        logger.info(f'patch -> v8_window.py -> Window.onunload -> get attr')

    def set_onunload(self, val):
        self._attr['onunload'] = val

    def get_crossOriginIsolated(self):
        val = self._attr.get('crossOriginIsolated')
        if val is not None:
            return val
        logger.info(f'patch -> v8_window.py -> Window.crossOriginIsolated -> get attr')

    def get_scheduler(self):
        val = self._attr.get('scheduler')
        if val is not None:
            return val
        logger.info(f'patch -> v8_window.py -> Window.scheduler -> get attr')

    def set_scheduler(self, val):
        self._attr['scheduler'] = val

    def get_originAgentCluster(self):
        val = self._attr.get('originAgentCluster')
        if val is not None:
            return val
        logger.info(f'patch -> v8_window.py -> Window.originAgentCluster -> get attr')

    def get_onorientationchange(self):
        val = self._attr.get('onorientationchange')
        if val is not None:
            return val
        logger.info(f'patch -> v8_window.py -> Window.onorientationchange -> get attr')

    def set_onorientationchange(self, val):
        self._attr['onorientationchange'] = val

    def get_orientation(self):
        val = self._attr.get('orientation')
        if val is not None:
            return val
        logger.info(f'patch -> v8_window.py -> Window.orientation -> get attr')

    def get_onpageswap(self):
        val = self._attr.get('onpageswap')
        if val is not None:
            return val
        logger.info(f'patch -> v8_window.py -> Window.onpageswap -> get attr')

    def set_onpageswap(self, val):
        self._attr['onpageswap'] = val

    def get_onpagereveal(self):
        val = self._attr.get('onpagereveal')
        if val is not None:
            return val
        logger.info(f'patch -> v8_window.py -> Window.onpagereveal -> get attr')

    def set_onpagereveal(self, val):
        self._attr['onpagereveal'] = val

    def get_defaultStatus(self):
        val = self._attr.get('defaultStatus')
        if val is not None:
            return val
        logger.info(f'patch -> v8_window.py -> Window.defaultStatus -> get attr')

    def set_defaultStatus(self, val):
        self._attr['defaultStatus'] = val

    def get_defaultstatus(self):
        val = self._attr.get('defaultstatus')
        if val is not None:
            return val
        logger.info(f'patch -> v8_window.py -> Window.defaultstatus -> get attr')

    def set_defaultstatus(self, val):
        self._attr['defaultstatus'] = val

    def get_credentialless(self):
        val = self._attr.get('credentialless')
        if val is not None:
            return val
        logger.info(f'patch -> v8_window.py -> Window.credentialless -> get attr')

    def get_ai(self):
        val = self._attr.get('ai')
        if val is not None:
            return val
        logger.info(f'patch -> v8_window.py -> Window.ai -> get attr')

    def set_ai(self, val):
        self._attr['ai'] = val

    def get_model(self):
        val = self._attr.get('model')
        if val is not None:
            return val
        logger.info(f'patch -> v8_window.py -> Window.model -> get attr')

    def set_model(self, val):
        self._attr['model'] = val

    def get_speechSynthesis(self):
        val = self._attr.get('speechSynthesis')
        if val is not None:
            return val
        logger.info(f'patch -> v8_window.py -> Window.speechSynthesis -> get attr')

    def get_onfencedtreeclick(self):
        val = self._attr.get('onfencedtreeclick')
        if val is not None:
            return val
        logger.info(f'patch -> v8_window.py -> Window.onfencedtreeclick -> get attr')

    def set_onfencedtreeclick(self, val):
        self._attr['onfencedtreeclick'] = val

    def get_onoverscroll(self):
        val = self._attr.get('onoverscroll')
        if val is not None:
            return val
        logger.info(f'patch -> v8_window.py -> Window.onoverscroll -> get attr')

    def set_onoverscroll(self, val):
        self._attr['onoverscroll'] = val

    def get_onscrollend(self):
        val = self._attr.get('onscrollend')
        if val is not None:
            return val
        logger.info(f'patch -> v8_window.py -> Window.onscrollend -> get attr')

    def set_onscrollend(self, val):
        self._attr['onscrollend'] = val

    def get_onscrollsnapchange(self):
        val = self._attr.get('onscrollsnapchange')
        if val is not None:
            return val
        logger.info(f'patch -> v8_window.py -> Window.onscrollsnapchange -> get attr')

    def set_onscrollsnapchange(self, val):
        self._attr['onscrollsnapchange'] = val

    def get_onscrollsnapchanging(self):
        val = self._attr.get('onscrollsnapchanging')
        if val is not None:
            return val
        logger.info(f'patch -> v8_window.py -> Window.onscrollsnapchanging -> get attr')

    def set_onscrollsnapchanging(self, val):
        self._attr['onscrollsnapchanging'] = val

    def get_onmove(self):
        val = self._attr.get('onmove')
        if val is not None:
            return val
        logger.info(f'patch -> v8_window.py -> Window.onmove -> get attr')

    def set_onmove(self, val):
        self._attr['onmove'] = val

    def get_ontimezonechange(self):
        val = self._attr.get('ontimezonechange')
        if val is not None:
            return val
        logger.info(f'patch -> v8_window.py -> Window.ontimezonechange -> get attr')

    def set_ontimezonechange(self, val):
        self._attr['ontimezonechange'] = val

    def get_crossOriginEmbedderPolicy(self):
        val = self._attr.get('crossOriginEmbedderPolicy')
        if val is not None:
            return val
        logger.info(f'patch -> v8_window.py -> Window.crossOriginEmbedderPolicy -> get attr')

    def get_translation(self):
        val = self._attr.get('translation')
        if val is not None:
            return val
        logger.info(f'patch -> v8_window.py -> Window.translation -> get attr')

    def set_translation(self, val):
        self._attr['translation'] = val

    def get_fence(self):
        val = self._attr.get('fence')
        if val is not None:
            return val
        logger.info(f'patch -> v8_window.py -> Window.fence -> get attr')

    def get_testOriginTrialGlobalAttribute(self):
        val = self._attr.get('testOriginTrialGlobalAttribute')
        if val is not None:
            return val
        logger.info(f'patch -> v8_window.py -> Window.testOriginTrialGlobalAttribute -> get attr')

    def get_caches(self):
        val = self._attr.get('caches')
        if val is not None:
            return val
        logger.info(f'patch -> v8_window.py -> Window.caches -> get attr')

    def get_cookieStore(self):
        val = self._attr.get('cookieStore')
        if val is not None:
            return val
        logger.info(f'patch -> v8_window.py -> Window.cookieStore -> get attr')

    def get_ondevicemotion(self):
        val = self._attr.get('ondevicemotion')
        if val is not None:
            return val
        logger.info(f'patch -> v8_window.py -> Window.ondevicemotion -> get attr')

    def set_ondevicemotion(self, val):
        self._attr['ondevicemotion'] = val

    def get_ondeviceorientation(self):
        val = self._attr.get('ondeviceorientation')
        if val is not None:
            return val
        logger.info(f'patch -> v8_window.py -> Window.ondeviceorientation -> get attr')

    def set_ondeviceorientation(self, val):
        self._attr['ondeviceorientation'] = val

    def get_ondeviceorientationabsolute(self):
        val = self._attr.get('ondeviceorientationabsolute')
        if val is not None:
            return val
        logger.info(f'patch -> v8_window.py -> Window.ondeviceorientationabsolute -> get attr')

    def set_ondeviceorientationabsolute(self, val):
        self._attr['ondeviceorientationabsolute'] = val

    def get_launchQueue(self):
        val = self._attr.get('launchQueue')
        if val is not None:
            return val
        logger.info(f'patch -> v8_window.py -> Window.launchQueue -> get attr')

    def get_privateAttribution(self):
        val = self._attr.get('privateAttribution')
        if val is not None:
            return val
        logger.info(f'patch -> v8_window.py -> Window.privateAttribution -> get attr')

    def set_privateAttribution(self, val):
        self._attr['privateAttribution'] = val

    def get_sharedStorage(self):
        val = self._attr.get('sharedStorage')
        if val is not None:
            return val
        logger.info(f'patch -> v8_window.py -> Window.sharedStorage -> get attr')

    def get_documentPictureInPicture(self):
        val = self._attr.get('documentPictureInPicture')
        if val is not None:
            return val
        logger.info(f'patch -> v8_window.py -> Window.documentPictureInPicture -> get attr')

    def get_ontouchcancel(self):
        val = self._attr.get('ontouchcancel')
        if val is not None:
            return val
        logger.info(f'patch -> v8_window.py -> Window.ontouchcancel -> get attr')

    def set_ontouchcancel(self, val):
        self._attr['ontouchcancel'] = val

    def get_ontouchend(self):
        val = self._attr.get('ontouchend')
        if val is not None:
            return val
        logger.info(f'patch -> v8_window.py -> Window.ontouchend -> get attr')

    def set_ontouchend(self, val):
        self._attr['ontouchend'] = val

    def get_ontouchmove(self):
        val = self._attr.get('ontouchmove')
        if val is not None:
            return val
        logger.info(f'patch -> v8_window.py -> Window.ontouchmove -> get attr')

    def set_ontouchmove(self, val):
        self._attr['ontouchmove'] = val

    def get_ontouchstart(self):
        val = self._attr.get('ontouchstart')
        if val is not None:
            return val
        logger.info(f'patch -> v8_window.py -> Window.ontouchstart -> get attr')

    def set_ontouchstart(self, val):
        self._attr['ontouchstart'] = val

    def fn_alert(self, *args):
        logger.info(f'patch -> v8_window.py -> Window.alert{tuple(args)} -> method')

    def fn_atob(self, *args):
        logger.info(f'patch -> v8_window.py -> Window.atob{tuple(args)} -> method')

    def fn_blur(self, *args):
        logger.info(f'patch -> v8_window.py -> Window.blur{tuple(args)} -> method')

    def fn_btoa(self, *args):
        logger.info(f'patch -> v8_window.py -> Window.btoa{tuple(args)} -> method')

    def fn_cancelAnimationFrame(self, *args):
        logger.info(f'patch -> v8_window.py -> Window.cancelAnimationFrame{tuple(args)} -> method')

    def fn_cancelIdleCallback(self, *args):
        logger.info(f'patch -> v8_window.py -> Window.cancelIdleCallback{tuple(args)} -> method')

    def fn_captureEvents(self, *args):
        logger.info(f'patch -> v8_window.py -> Window.captureEvents{tuple(args)} -> method')

    def fn_clearInterval(self, *args):
        logger.info(f'patch -> v8_window.py -> Window.clearInterval{tuple(args)} -> method')

    def fn_clearTimeout(self, *args):
        logger.info(f'patch -> v8_window.py -> Window.clearTimeout{tuple(args)} -> method')

    def fn_close(self, *args):
        logger.info(f'patch -> v8_window.py -> Window.close{tuple(args)} -> method')

    def fn_confirm(self, *args):
        logger.info(f'patch -> v8_window.py -> Window.confirm{tuple(args)} -> method')

    def fn_createImageBitmap(self, *args):
        logger.info(f'patch -> v8_window.py -> Window.createImageBitmap{tuple(args)} -> method')

    def fn_fetch(self, *args):
        logger.info(f'patch -> v8_window.py -> Window.fetch{tuple(args)} -> method')

    def fn_find(self, *args):
        logger.info(f'patch -> v8_window.py -> Window.find{tuple(args)} -> method')

    def fn_focus(self, *args):
        logger.info(f'patch -> v8_window.py -> Window.focus{tuple(args)} -> method')

    def fn_getComputedStyle(self, *args):
        logger.info(f'patch -> v8_window.py -> Window.getComputedStyle{tuple(args)} -> method')

    def fn_getSelection(self, *args):
        logger.info(f'patch -> v8_window.py -> Window.getSelection{tuple(args)} -> method')

    def fn_matchMedia(self, *args):
        logger.info(f'patch -> v8_window.py -> Window.matchMedia{tuple(args)} -> method')

    def fn_moveBy(self, *args):
        logger.info(f'patch -> v8_window.py -> Window.moveBy{tuple(args)} -> method')

    def fn_moveTo(self, *args):
        logger.info(f'patch -> v8_window.py -> Window.moveTo{tuple(args)} -> method')

    def fn_open(self, *args):
        logger.info(f'patch -> v8_window.py -> Window.open{tuple(args)} -> method')

    def fn_postMessage(self, *args):
        logger.info(f'patch -> v8_window.py -> Window.postMessage{tuple(args)} -> method')

    def fn_print(self, *args):
        logger.info(f'patch -> v8_window.py -> Window.print{tuple(args)} -> method')

    def fn_prompt(self, *args):
        logger.info(f'patch -> v8_window.py -> Window.prompt{tuple(args)} -> method')

    def fn_queueMicrotask(self, *args):
        logger.info(f'patch -> v8_window.py -> Window.queueMicrotask{tuple(args)} -> method')

    def fn_releaseEvents(self, *args):
        logger.info(f'patch -> v8_window.py -> Window.releaseEvents{tuple(args)} -> method')

    def fn_reportError(self, *args):
        logger.info(f'patch -> v8_window.py -> Window.reportError{tuple(args)} -> method')

    def fn_requestAnimationFrame(self, *args):
        logger.info(f'patch -> v8_window.py -> Window.requestAnimationFrame{tuple(args)} -> method')

    def fn_requestIdleCallback(self, *args):
        logger.info(f'patch -> v8_window.py -> Window.requestIdleCallback{tuple(args)} -> method')

    def fn_resizeBy(self, *args):
        logger.info(f'patch -> v8_window.py -> Window.resizeBy{tuple(args)} -> method')

    def fn_resizeTo(self, *args):
        logger.info(f'patch -> v8_window.py -> Window.resizeTo{tuple(args)} -> method')

    def fn_scroll(self, *args):
        logger.info(f'patch -> v8_window.py -> Window.scroll{tuple(args)} -> method')

    def fn_scrollBy(self, *args):
        logger.info(f'patch -> v8_window.py -> Window.scrollBy{tuple(args)} -> method')

    def fn_scrollTo(self, *args):
        logger.info(f'patch -> v8_window.py -> Window.scrollTo{tuple(args)} -> method')

    def fn_setInterval(self, *args):
        logger.info(f'patch -> v8_window.py -> Window.setInterval{tuple(args)} -> method')

    def fn_setTimeout(self, *args):
        logger.info(f'patch -> v8_window.py -> Window.setTimeout{tuple(args)} -> method')

    def fn_stop(self, *args):
        logger.info(f'patch -> v8_window.py -> Window.stop{tuple(args)} -> method')

    def fn_structuredClone(self, *args):
        logger.info(f'patch -> v8_window.py -> Window.structuredClone{tuple(args)} -> method')

    def fn_webkitCancelAnimationFrame(self, *args):
        logger.info(f'patch -> v8_window.py -> Window.webkitCancelAnimationFrame{tuple(args)} -> method')

    def fn_webkitRequestAnimationFrame(self, *args):
        logger.info(f'patch -> v8_window.py -> Window.webkitRequestAnimationFrame{tuple(args)} -> method')

    def fn_getComputedAccessibleNode(self, *args):
        logger.info(f'patch -> v8_window.py -> Window.getComputedAccessibleNode{tuple(args)} -> method')

    def fn_webkitRequestFileSystem(self, *args):
        logger.info(f'patch -> v8_window.py -> Window.webkitRequestFileSystem{tuple(args)} -> method')

    def fn_webkitResolveLocalFileSystemURL(self, *args):
        logger.info(f'patch -> v8_window.py -> Window.webkitResolveLocalFileSystemURL{tuple(args)} -> method')

    def fn_fetchLater(self, *args):
        logger.info(f'patch -> v8_window.py -> Window.fetchLater{tuple(args)} -> method')

    def fn_getDigitalGoodsService(self, *args):
        logger.info(f'patch -> v8_window.py -> Window.getDigitalGoodsService{tuple(args)} -> method')

    def fn_getLockScreenData(self, *args):
        logger.info(f'patch -> v8_window.py -> Window.getLockScreenData{tuple(args)} -> method')

    def fn_getScreenDetails(self, *args):
        logger.info(f'patch -> v8_window.py -> Window.getScreenDetails{tuple(args)} -> method')

    def fn_maximize(self, *args):
        logger.info(f'patch -> v8_window.py -> Window.maximize{tuple(args)} -> method')

    def fn_minimize(self, *args):
        logger.info(f'patch -> v8_window.py -> Window.minimize{tuple(args)} -> method')

    def fn_restore(self, *args):
        logger.info(f'patch -> v8_window.py -> Window.restore{tuple(args)} -> method')

    def fn_setResizable(self, *args):
        logger.info(f'patch -> v8_window.py -> Window.setResizable{tuple(args)} -> method')

    def fn_openDatabase(self, *args):
        logger.info(f'patch -> v8_window.py -> Window.openDatabase{tuple(args)} -> method')

    def fn_queryLocalFonts(self, *args):
        logger.info(f'patch -> v8_window.py -> Window.queryLocalFonts{tuple(args)} -> method')

    def fn_showDirectoryPicker(self, *args):
        logger.info(f'patch -> v8_window.py -> Window.showDirectoryPicker{tuple(args)} -> method')

    def fn_showOpenFilePicker(self, *args):
        logger.info(f'patch -> v8_window.py -> Window.showOpenFilePicker{tuple(args)} -> method')

    def fn_showSaveFilePicker(self, *args):
        logger.info(f'patch -> v8_window.py -> Window.showSaveFilePicker{tuple(args)} -> method')
