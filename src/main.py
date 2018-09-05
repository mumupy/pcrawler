#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/8/1 21:08
# @Author  : ganliang
# @File    : Crawler.py
# @Desc    : 爬虫核心入口
import os
import sys

# 将项目添加到pythonpath环境变量中
project_dir = os.path.dirname(os.getcwd())
sys.path.append(project_dir)
print(sys.path)


def runner():
    print("hello world")


if __name__ == "__main__":
    runner()
