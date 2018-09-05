#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/8/15 13:06
# @Author  : ganliang
# @File    : MediaStorageTest.py
# @Desc    : 多媒体内容下载测试代码

from src.storage.basic.MediaStorage import MediaStorage


def storage():
    mediaStorage = MediaStorage("./", "html")
    mediaStorage.storage({"html": "https://www.cnblogs.com/swordxia/p/4666231.html"})

if __name__=="__main__":
    storage()