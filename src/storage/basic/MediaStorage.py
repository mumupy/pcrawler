#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/8/14 23:13
# @Author  : ganliang
# @File    : MediaStorage.py
# @Desc    : 图片、视频存储器
import os
import urllib2

from src.config.Config import logging
from src.storage.Storage import Storage


class MediaStorage(Storage):
    """将url链接下载下来 存储到文件中"""

    def __init__(self, out_path, attach=False):
        """
            out_path 文件输出路径
            attach 保存文件时 是否携带url路径
        """
        if not os.path.exists(out_path):
            os.makedirs(out_path)
        self.out_path = out_path

    def storage(self, field_dict):
        if not field_dict:
            return

        for field_name in field_dict:
            field_values = field_dict.get(field_name)
            if not isinstance(field_values, list):
                media_urls = [field_values]
            for field_value in field_values:
                # 获取url路径名称
                try:
                    logging.info(field_value)
                    # 下载内容信息
                    content = urllib2.urlopen(field_value).read()
                    # 将内容写入到文件中
                    media_file = open(os.path.join(self.out_path, os.path.split(field_value)[1]), "w")
                    media_file.writelines(content)
                    media_file.close()
                except Exception as ex:
                    logging.error(ex)
