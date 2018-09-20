#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/9/3 9:37
# @Author  : ganliang
# @File    : CsvStorage.py
# @Desc    : 将爬去的字段信息保存到csv文件中
import os
import threading
import time

from src.storage.Storage import Storage
from src.config.Config import logging

class CsvStorage(Storage):
    """使用csv格式存储文件"""

    def __init__(self, csv_path, file_counter=10000):
        self.csv_path = csv_path
        if not os.path.exists(self.csv_path):
            os.makedirs(self.csv_path)

        self.file_counter = file_counter
        self.current_counter = 0
        self.csv_headers = []  # csv文件头
        self.csv_writer = None  # csv
        self.storage_lock = threading.Lock()

    def get_csv_file(self, field_dict):
        # 如果文件存在 则关闭文件
        if self.csv_writer:
            self.csv_writer.close()
        # 将第一条记录的字段放置到文件文件头上
        if len(self.csv_headers) == 0:
            for field_key in field_dict:
                self.csv_headers.append(field_key)
        # 生成csv文件
        csv_file = os.path.join(self.csv_path, str(int(time.time() * 1000)) + ".csv")
        self.csv_writer = open(csv_file, "w")
        # 将头信息写入到csv中
        self.csv_writer.write("|".join(self.csv_headers) + "\n")

    def storage(self, field_dict):
        if not field_dict:
            return

        # 获取csv文件
        if self.current_counter % self.file_counter == 0:
            self.get_csv_file(field_dict)
        # 从字典中获取到字段指
        field_values = []
        for csv_header in self.csv_headers:
            field_values.append(field_dict.get(csv_header, ""))
        self.csv_writer.write("|".join(field_values) + "\n")

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.csv_writer.close()
        logging.info("__exit__")
