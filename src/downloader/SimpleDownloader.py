#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/8/13 21:11
# @Author  : ganliang
# @File    : SimpleDownloader.py
# @Desc    : 基本下载器
import urllib2

from src.config.Config import logging


class SimpleDownloader:
    """基本下载器"""

    def download(self, url):
        """下载html 返回html内容"""
        try:
            content = str(urllib2.urlopen(url, timeout=5).read())
            # 获取html内容的content-type标签 找到html编码
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
