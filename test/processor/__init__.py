#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/8/16 13:47
# @Author  : ganliang
# @File    : __init__.py.py
# @Desc    : TODO
import os

url = "http://www.nsfocus.net"
a_element = "../value"

a_element = os.path.join(url, a_element).replace("\\", "/")
print(a_element)
relative_index = a_element.find("/../")
if relative_index > -1:
    a_element = a_element[:relative_index] + a_element[relative_index+3:]
    print(a_element)