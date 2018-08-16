#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/8/16 12:50
# @Author  : ganliang
# @File    : NsfocusLoopholePageProcess.py
# @Desc    : 绿盟漏洞爬虫业务类
from src.config.Config import logging
from src.processor.PageProcess import PageProcess


class NsfocusLoopholePageProcess(PageProcess):
    """绿盟漏洞爬虫业务类"""

    def process(self, page):
        res_html = self.handler(page)
        vulbar_content = res_html.xpath("//div[@class='vulbar']/text()")
        logging.info(vulbar_content)
        page.put_field("vulbar", vulbar_content)
