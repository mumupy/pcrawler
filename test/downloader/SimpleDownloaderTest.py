#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/8/15 21:58
# @Author  : ganliang
# @File    : SimpleDownloaderTest.py
# @Desc    : 基本下载器测试
import threading
import time
import urllib2

import chardet

from src.config.Config import logging


def detect(content):
    """使用chardect获取文本编码 然后在解码 但是在多线程情况下chardet特别忙（怀疑是线程锁同步问题）"""
    char_encoding = chardet.detect(content)
    encoding = char_encoding.get("encoding", "utf-8")
    if str(encoding).upper() == "GB2312":
        encoding = "gbk"
    return unicode(content, encoding=encoding)


def download(url):
    """下载html 返回html内容"""
    try:
        content = str(urllib2.urlopen(url, timeout=5).read())
        content_type_start_index = content.find("Content-Type")
        if content_type_start_index > -1:
            charset_start_index = content.find("charset=", content_type_start_index)
            content_type_end_index = content.find(">", content_type_start_index)
            encoding = content[charset_start_index + len("charset="):content_type_end_index - 3]
            if str(encoding).upper() == "GB2312":
                encoding = "gbk"
            content = unicode(content, encoding=encoding)
        return content
    except Exception as ex:
        logging.error(ex)
    return None


if __name__ == "__main__":
    for i in range(1):
        threading.Thread(target=download, args=("http://hb.sina.com.cn/news/i/2012-05-21/75211.html",)).start()
