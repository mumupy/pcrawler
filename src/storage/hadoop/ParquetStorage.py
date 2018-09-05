#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/9/3 13:15
# @Author  : ganliang
# @File    : ParquetStorage.py
# @Desc    : parquet列族存储
import os
import threading

from src.storage.Storage import Storage


class ParquetStorage(Storage):
    def __init__(self, parquet_path, file_counter=10000):
        self.parquet_path = parquet_path
        if not os.path.exists(self.parquet_path):
            os.makedirs(self.parquet_path)

        self.file_counter = file_counter
        self.current_counter = 0
        self.parquet_writer = None  # parquet文件
        self.storage_lock = threading.Lock()
