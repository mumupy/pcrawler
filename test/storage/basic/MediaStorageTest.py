#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/8/15 13:06
# @Author  : ganliang
# @File    : MediaStorageTest.py
# @Desc    : 多媒体内容下载测试代码
import urllib2

import requests

from src.storage.basic.MediaStorage import MediaStorage


def storage():
    mediaStorage = MediaStorage("./", "html")
    mediaStorage.storage({"html": "https://www.cnblogs.com/swordxia/p/4666231.html"})


def downloadImg(url):
    content = urllib2.urlopen(url).read()
    with open(url[url.rfind("/") + 1:], "wb") as media_file:
        media_file.write(content)


if __name__ == "__main__":
    # storage()
    downloadImg("http://www.xiaohuar.com/d/file/20161102/4bb76725c4d4ac5077b9a1c594c5cbb2.jpg")
    downloadImg("http://pic1.win4000.com/tj/2018-05-08/5af161802bcc1.jpg")
