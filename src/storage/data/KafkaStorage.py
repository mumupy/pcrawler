#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/6/22 12:20
# @Author  : ganliang
# @File    : KafkaStorage.py
# @Desc    : kafka存储
import json

from src.config.Config import logging
from src.storage.Storage import Storage


class KafkaStorage(Storage):
    """
    将数据存储到kafka中
    """

    def __init__(self, **kwargs):
        super(KafkaStorage, self).__init__()

    def storage(self, field_dict):
        if field_dict:
            if isinstance(field_dict, dict):
                logging.info(json.dumps(field_dict, ensure_ascii=False))
            else:
                logging.info(field_dict)
