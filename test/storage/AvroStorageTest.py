#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/9/2 19:46
# @Author  : ganliang
# @File    : AvroStorageTest.py
# @Desc    : avro测试代码
import unittest
from src.storage.hadoop.AvroStorage import AvroStorage
from src.config.Config import logging


class AvroStorageTest(unittest.TestCase):

    def setUp(self):
        self.avroStorage = AvroStorage("./")

    def test_get_file_properties(self):
        json_data = {}
        fields = self.avroStorage.get_file_properties(json_data)
        logging.info(fields)

    def test_storage(self):
        json_data = {}
        self.avroStorage.storage(json_data)

if __name__ == "__main__":
    unittest.main()
