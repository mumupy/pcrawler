#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/5 0:10
# @Author  : ganliang
# @File    : VedioPageProcessTest.py
# @Desc    : TODO
from src.core.Page import Page
from src.processor.builtin.VedioPageProcess import VedioPageProcess


def process(url):
    vedioPageProcess = VedioPageProcess()

    page = Page(url, self.crawler.base_url, None, self.crawler).setContent(content)





if __name__ == "__main__":
    process("http://www.xj940.com/player/index15813.html?15813-0-0")