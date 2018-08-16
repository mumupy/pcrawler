#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/8/16 12:50
# @Author  : ganliang
# @File    : NsfocusLoopholePageProcess.py
# @Desc    : 绿盟漏洞爬虫业务类
from lxml import etree

from src.processor.PageProcess import PageProcess
from src.util.ElementUtil import getElement


class NsfocusLoopholePageProcess(PageProcess):
    """绿盟漏洞爬虫业务类"""

    def process(self, page):
        res_html = self.handler(page)

        loophole_title = getElement(res_html, "//div[@class='title']/text()")
        if loophole_title.find("安全漏洞") == -1:
            return

        vulbar_content_element = res_html.xpath("//div[@class='vulbar']")[0]

        title = getElement(vulbar_content_element, "//div[@align='center']/b/text()")
        if not title:
            return
        page.put_field("title", title)

        refect_product = getElement(vulbar_content_element, "//blockquote/text()")
        page.put_field("refect_product", str(refect_product))

        links = vulbar_content_element.xpath("a/@href")
        cve_link, vender_link, advisory_link = None, None, None
        if len(links) == 3:
            cve_link, vender_link, advisory_link = links
        elif len(links) == 2:
            cve_link, advisory_link = links
        elif len(links) == 1:
            cve_link = links
        cve_id = getElement(vulbar_content_element, "a/text()")
        page.put_field("cve_link", cve_link)
        page.put_field("cve_id", cve_id)
        page.put_field("vender_link", vender_link)
        page.put_field("advisory_link", advisory_link)

        main_content = etree.tostring(vulbar_content_element, encoding="utf-8")
        main_content = str(main_content)

        pubdate_index = main_content.find("发布日期")
        pubdate_before_index = main_content.find(">", pubdate_index) + 1
        pubdate_after_index = main_content.find("<", pubdate_before_index)
        pubdate = main_content[pubdate_before_index:pubdate_after_index]
        page.put_field("pubdate", pubdate)

        update_index = main_content.find("更新日期")
        update_before_index = main_content.find(">", update_index) + 1
        update_after_index = main_content.find("<", update_before_index)
        update_date = main_content[update_before_index:update_after_index]
        page.put_field("update_date", update_date)

        desc_index = main_content.find("描述：")
        desc_before_index = main_content.find("<br/>", desc_index) + 12
        desc_after_index = main_content.find("<br/>&#13;", desc_before_index)
        desc = main_content[desc_before_index:desc_after_index]

        desc_before_index = main_content.find("<br/>&#13;", desc_after_index) + 23
        desc_after_index = main_content.find("<br/>", desc_before_index)
        desc2 = main_content[desc_before_index:desc_after_index]
        page.put_field("desc", desc + desc2)

        advisory_begin_index = main_content.rfind("厂商补丁：<br/>") + len("厂商补丁：<br/>") + 6
        advisory_end_index = main_content.rfind("&#13;")
        advisory = main_content[advisory_begin_index:advisory_end_index]
        page.put_field("advisory", advisory)
