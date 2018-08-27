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

    vulbar_content_elements = res_html.xpath("//div[@class='vulbar']")
    if not vulbar_content_elements:
        return
    vulbar_content_element = vulbar_content_elements[0]
    title = getElement(vulbar_content_element, "//div[@align='center']/b/text()")
    logging.info("title:" + title)

    refect_product = getElement(vulbar_content_element, "//blockquote/text()")
    logging.info("refect_product:" + refect_product)

    cve_link, vender_link, advisory_link = vulbar_content_element.xpath("a/@href")
    cve_id = vulbar_content_element.xpath("a/text()")[0]
    logging.info("cve_link:" + cve_link)
    logging.info("cve_id:" + cve_id)
    logging.info("vender_link:" + vender_link)
    logging.info("advisory_link:" + advisory_link)

    main_content = etree.tostring(vulbar_content_element, encoding="utf-8").decode("utf-8")
    main_content = str(main_content)

    pubdate_index = main_content.find("发布日期")
    pubdate_before_index = main_content.find(">", pubdate_index) + 1
    pubdate_after_index = main_content.find("<", pubdate_before_index)
    pubdate = main_content[pubdate_before_index:pubdate_after_index]
    logging.info("pubdate:" + pubdate)

    update_index = main_content.find("更新日期")
    update_before_index = main_content.find(">", update_index) + 1
    update_after_index = main_content.find("<", update_before_index)
    update_date = main_content[update_before_index:update_after_index]
    logging.info("update_date:" + update_date)

    desc_index = main_content.find("描述：")
    desc_before_index = main_content.find("<br/>", desc_index) + 12
    desc_after_index = main_content.find("<br/>&#13;", desc_before_index)
    desc = main_content[desc_before_index:desc_after_index]
    logging.info("desc:" + desc)

    desc_before_index = main_content.find("<br/>&#13;", desc_after_index) + 23
    desc_after_index = main_content.find("<br/>", desc_before_index)
    desc2 = main_content[desc_before_index:desc_after_index]
    logging.info("desc:" + desc2)

    advisory_begin_index = main_content.rfind("厂商补丁：<br/>") + len("厂商补丁：<br/>") + 6
    advisory_end_index = main_content.rfind("&#13;")
    advisory = main_content[advisory_begin_index:advisory_end_index]
    logging.info("advisory:" + advisory)


if __name__ == "__main__":
    process("http://www.nsfocus.net/?act=advisory&do=view&adv_id=100")
