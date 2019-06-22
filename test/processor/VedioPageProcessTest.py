#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/5 0:10
# @Author  : ganliang
# @File    : VedioPageProcessTest.py
# @Desc    : 视频下载
from src.core.Page import Page
from src.processor.builtin.VedioPageProcess import VedioPageProcess


def process(url):
    vedioPageProcess = VedioPageProcess()