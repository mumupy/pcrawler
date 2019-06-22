#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/8/1 21:07
# @Author  : ganliang
# @File    : __init__.py.py
# @Desc    : pcrawler爬虫程序


# __all__ = ["main", "config", "core", "downloader", "monitor", "processor", "scheduler", "storage", "util"]
# __all__ = ["main"]

scope = {}
exec ("import os ;os.system('dir')", scope)
print(scope)

scope.setdefault("i", 5)
scope.setdefault("j", 7)
print(eval("i*j", scope))

data = [('a', 1), ('b', 2), ('c', 3), ('d', 10), ('a', 2), ('c', 4)]

wordcount_map = {}


def rd(x, y):
    if x:
        counter = wordcount_map.get(x[0], 0)
        counter += x[1]
        wordcount_map[x[0]] = counter

    if y:
        ycounter = wordcount_map.get(y[0], 0)
        ycounter += y[1]
        wordcount_map[y[0]] = ycounter

    return None


print(wordcount_map)
print(filter(lambda x: x[1] > 5, wordcount_map.items()))