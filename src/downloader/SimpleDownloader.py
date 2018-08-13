#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/8/13 21:11
# @Author  : ganliang
# @File    : SimpleDownloader.py
# @Desc    : 基本下载器
import urllib2

import chardet

from src.config.Config import logging


class SimpleDownloader:
    """基本下载器"""

    def download(self, url):
        """下载html 返回html内容"""
        try:
            content = urllib2.urlopen(url).read()
            char_encoding = chardet.detect(content)
            encoding = char_encoding.get("encoding", "utf-8")
            if str(encoding).upper() == "GB2312":
                encoding = "gbk"
            return unicode(content, encoding=encoding)
        except Exception as ex:
            logging.error(ex)
        return None
