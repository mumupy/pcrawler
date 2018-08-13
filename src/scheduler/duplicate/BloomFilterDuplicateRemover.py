#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/8/13 19:23
# @Author  : ganliang
# @File    : BloomFilterDuplicateRemover.py
# @Desc    : bloomFilter数据去重
from pybloom import BloomFilter
from src.scheduler.duplicate.DuplicateRemover import DuplicateRemover

class BloomFilterDuplicateRemover(DuplicateRemover):

    def __init__(self, capacity=1000000, error_rate=0.001):
        self.bloomFilter = BloomFilter(capacity, error_rate)

    def dump(self, url):
        url_hash = abs(hash(url))
        return self.bloomFilter.add(url_hash)


if __name__ == "__main__":
    dump = BloomFilterDuplicateRemover()
    print(dump.dump("123"))
    print(dump.dump("123"))
