#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/9/21 17:32
# @Author  : ganliang
# @File    : conf.py
# @Desc    : 将md文档转化为rst文档

from recommonmark.parser import CommonMarkParser

source_parsers = {
    '.md': CommonMarkParser,
}

source_suffix = ['.rst', '.md']