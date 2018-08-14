#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/8/13 21:48
# @Author  : ganliang
# @File    : ConsoleStorage.py
# @Desc    : 将爬取得内容打印在控制台
import json

from src.config.Config import logging
from src.storage.Storage import Storage


class ConsoleStorage(Storage):
    """将数据直接打印在控制台"""

    def storage(self, field_dict):
        if field_dict:
            logging.info(json.dumps(field_dict,ensure_ascii=False))
