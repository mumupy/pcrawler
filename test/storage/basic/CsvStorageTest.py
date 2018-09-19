#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/9/3 13:01
# @Author  : ganliang
# @File    : CsvStorageTest.py
# @Desc    : csv存储测试
import unittest

from src.storage.basic.CsvStorage import CsvStorage


class CsvStorageTest(unittest.TestCase):

    def setUp(self):
        self.csv_storage = CsvStorage("./")

    def test_get_csv_file(self):
        field_dict = {"name": "ganliang", "lover": "cws", "sex": "man"}
        self.csv_storage.get_csv_file(field_dict)

    def test_storage(self):
        field_dict = {"name": "ganliang", "lover": "cws", "sex": "man"}
        self.csv_storage.storage(field_dict)


if __name__ == "__main__":
    unittest.main()
