# import requests
from curl_cffi import requests


class DownloadHandler:

    def __init__(self, url=None, headers=None, proxies=None):
        self._cookies = {}
        self.s = requests.Session()
        self.headers = headers or {}
        self.url = url
        self.proxies = proxies

    def html(self, url=None, headers=None):
        url = url or self.url
        if not url:
            raise Exception("参数错误，请设置url")
        headers = headers or self.headers
        res = self.s.get(url, headers=headers, proxies=self.proxies)
        return res.text

    def js(self, src, headers=None):
        return self.s.get(src, headers=headers or self.headers, proxies=self.proxies).text

    @property
    def cookies(self):
        return {}
        # return dict(self.s.cookies)
