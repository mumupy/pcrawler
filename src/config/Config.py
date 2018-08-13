#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/8/12 13:16
# @Author  : ganliang
# @File    : Config.py
# @Desc    : 基本配置信息
import logging

LOGGING_CONFIG = {
    # "filename": "config.log",
    # "filemode": "w",
    "format": "%(asctime)s|%(process)d|%(thread)d|%(filename)s[%(funcName)s:%(lineno)d]|%(levelname)s|%(message)s",
    "level": logging.INFO
}
logging.basicConfig(**LOGGING_CONFIG)

logging = logging

__all__ = ["logging"]
