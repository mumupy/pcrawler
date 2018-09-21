#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/9/19 8:54
# @Author  : ganliang
# @File    : crawler.py
# @Desc    : 启动脚本程序
import os
import sys

# 将项目添加到pythonpath环境变量中
project_dir = os.path.dirname(__file__)
sys.path.append(project_dir)

from src.main import *


def __crawler_news__(args):
    if len(args) >= 2:
        params = {}
        url, outpath = args[:2]
        if len(args) == 2:
            pass
        elif len(args) == 3:
            params.setdefault("thread_count", args[-1])
        elif len(args) == 4:
            params.setdefault("thread_count", args[-2])
            params.setdefault("storage", args[-1])
        elif len(args) == 5:
            params.setdefault("thread_count", args[-3])
            params.setdefault("storage", args[-2])
            params.setdefault("duplicateRemover", args[-1])
        else:
            logging.warn("usage: python crawler.py news url outpath thread_count storage duplicateRemover")
            sys.exit(-1)
        crawler_news(url, __get_outpath__(outpath), **params)
    else:
        logging.warn("usage: python crawler.py news url outpath")


def __crawler_image__(args):
    if len(args) >= 2:
        params = {}
        url, outpath = args[:2]
        if len(args) == 2:
            pass
        elif len(args) == 3:
            params.setdefault("thread_count", args[-1])
        elif len(args) == 4:
            params.setdefault("thread_count", args[-2])
            params.setdefault("storage", args[-1])
        elif len(args) == 5:
            params.setdefault("thread_count", args[-3])
            params.setdefault("storage", args[-2])
            params.setdefault("duplicateRemover", args[-1])
        else:
            logging.warn("usage: python crawler.py image url outpath thread_count storage duplicateRemover")
            sys.exit(-1)
        crawler_images(url, __get_outpath__(outpath), **params)
    else:
        logging.warn("usage: python crawler.py image url outpath")


def __crawler_video__(args):
    if len(args) >= 2:
        params = {}
        url, outpath = args[:2]
        if len(args) == 2:
            pass
        elif len(args) == 3:
            params.setdefault("thread_count", args[-1])
        elif len(args) == 4:
            params.setdefault("thread_count", args[-2])
            params.setdefault("duplicateRemover", args[-1])
        else:
            logging.warn("usage: python crawler.py video url outpath thread_count duplicateRemover")
            sys.exit(-1)
        crawler_video(url, __get_outpath__(outpath), **params)
    else:
        logging.warn("usage: python crawler.py video url outpath")


def __crawler_nsfocus__(args):
    if len(args) >= 1:
        params = {}
        outpath = args[0]
        if len(args) == 1:
            pass
        elif len(args) == 2:
            params.setdefault("thread_count", args[-1])
        elif len(args) == 3:
            params.setdefault("thread_count", args[-2])
            params.setdefault("duplicateRemover", args[-1])
        elif len(args) == 4:
            params.setdefault("thread_count", args[-3])
            params.setdefault("storage", args[-2])
            params.setdefault("duplicateRemover", args[-1])
        else:
            logging.warn("usage: python crawler.py nsfocus outpath thread_count storage duplicateRemover")
            sys.exit(-1)
        crawler_nsfocus_loophole(__get_outpath__(outpath), **params)
    else:
        logging.warn("usage: python crawler.py nsfocus outpath")


def __get_outpath__(outpath):
    if str(outpath).startswith("/"):
        return outpath
    else:
        return os.path.join(os.path.dirname(__file__), outpath).replace("\\","/")


if __name__ == "__main__":
    args = sys.argv[1:]
    operation = str(args[0]).upper() if len(args) > 0 else ""
    if operation == "NEWS":  # 将es数据导入
        __crawler_news__(args[1:])
    elif operation == "IMAGE":
        __crawler_image__(args[1:])
    elif operation == "VIDEO":
        __crawler_video__(args[1:])
    elif operation == "NSFOCUS":
        __crawler_nsfocus__(args[1:])
    else:
        logging.warn("usage: python crawler.py news|image|video|nsfocus")
