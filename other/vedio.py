#-*-coding:utf-8 -8-
import requests
import re
import json
from bs4 import BeautifulSoup


class video_downloader():
    def __init__(self, url):
        self.server = 'http://api.xfsub.com'
        self.api = 'http://api.xfsub.com/xfsub_api/?url='
        self.get_url_api = 'http://api.xfsub.com/xfsub_api/url.php'
        self.url = url.split('#')[0]
        self.target = self.api+self.url
        self.s = request.session()

    def get_key(self):
        req = self.s.get(url=self.target)
        req.encoding = 'utf-8'
        self.info = json.loads(re.findall('"url.php",\(.+),', req.text))[0]
