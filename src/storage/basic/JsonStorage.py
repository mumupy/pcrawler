#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/8/3 22:23
# @Author  : ganliang
# @File    : JsonStorage.py
# @Desc    : json文本存储器
import json
import os
import threading
import time
import traceback

from src.config.Config import logging
from src.storage.Storage import Storage


class JsonStorage(Storage):
    """将数据按照json的格式存储到文件中"""

    def __init__(self, json_path, file_counter=10000):
        self.json_path = json_path
        if not os.path.exists(self.json_path):
            os.makedirs(self.json_path)
        self.file_counter = file_counter
        self.current_counter = 0
        self.json_file = open(os.path.join(self.json_path, str(int(time.time() * 1000)) + ".json"), "w")
        self.storage_lock = threading.Lock()

    def storage(self, json_data):
        if not json_data:
            return

        # 判断文件是否写满 放置到锁同步中 防止产生空文件
        try:
            self.storage_lock.acquire()
            if self.current_counter >= self.file_counter:
                self.json_file.close()
                self.json_file = open(os.path.join(self.json_path, str(int(time.time() * 1000)) + ".json"), "w")
                self.current_counter = 0

            article = json.dumps(json_data, ensure_ascii=False)
            logging.info(article)
            self.json_file.write(article + "\n")
            self.current_counter += 1
        except Exception as ex:
            traceback.print_exc()
        finally:
            self.storage_lock.release()
