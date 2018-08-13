#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/8/12 22:01
# @Author  : ganliang
# @File    : Install.py
# @Desc    : 安装器
import os

def install():
    os.system("pip install lxml")
    os.system("pip install pybloom")
    os.system("pip install chardet")

if __name__ == "__main__":
    install()