#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/8/16 13:47
# @Author  : ganliang
# @File    : NsfocusLoopholePageProcessTest.py
# @Desc    : 绿盟漏洞测试
from lxml import etree

from src.config.Config import logging
from src.downloader.SimpleDownloader import SimpleDownloader
from src.util.ElementUtil import getElement

def process(url):
    simpleDownloader = SimpleDownloader()
    content = simpleDownloader.download(url)
    res_html = etree.HTML(content)

    vulbar_content_element = res_html.xpath("//div[@class='vulbar']")[0]

    title=getElement(vulbar_content_element,"//div[@align='center']/b/text()")
    refect_product=getElement(vulbar_content_element,"//blockquote/text()")
    print(title)
    print(refect_product)

    links=vulbar_content_element.xpath("//a/@href")
    print(links)

    vulbar_content = res_html.xpath("//div[@class='vulbar']/text()")
    for content in vulbar_content:
        if content=="\r\n" or content=="\r" or content=="\n" or content==" ":
            continue
        # print(content)
if __name__ == "__main__":
    process("http://www.nsfocus.net/vulndb/40806")
