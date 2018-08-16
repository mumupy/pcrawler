#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/8/2 21:51
# @Author  : ganliang
# @File    : ElementUtil.py
# @Desc    : 元素工具类

def getElement(res_html, xpath):
    if res_html is None:
        return ""
    if isinstance(res_html, list):
        res_html = res_html[0]
    tag_elements = res_html.xpath(xpath)
    if not tag_elements:
        return ""
    tag_element = tag_elements[0]
    return tag_element


__all__ = ["getElement"]
