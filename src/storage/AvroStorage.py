#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/8/24 15:58
# @Author  : ganliang
# @File    : AvroStorage.py
# @Desc    : 使用avro格式来存储
import json
import os
import threading
import time
import traceback

import avro.schema
from avro.datafile import DataFileWriter
from avro.io import DatumWriter

from src.config.Config import logging
from src.storage.Storage import Storage


class AvroStorage(Storage):

    def __init__(self, avro_path, file_counter=10000):
        self.avro_path = avro_path
        if not os.path.exists(self.avro_path):
            os.makedirs(self.avro_path)
        self.file_counter = file_counter
        self.current_counter = 0
        self.avro_writer = None  # avro文件
        self.storage_lock = threading.Lock()

    def get_file_properties(self, json_data):
        """从字典中获取文件字段属性"""
        fields = []
        logging.info(json_data)
        for json_key in json_data.keys():
            value = json_data.get(json_key)
            if isinstance(value, int):
                fields.append((json_key, ["int", "long"]))
            elif isinstance(value, float):
                fields.append((json_key, "float"))
            elif isinstance(value, long):
                fields.append((json_key, "long"))
            else:
                fields.append((json_key, "string"))
        return fields

    def set_avro_writer(self, json_data):
        """设置avro文件"""
        avro_schema_fields = self.get_file_properties(json_data)
        avro_schema = {"namespace": "data.avro",
                       "type": "record",
                       "name": "hbnews",
                       "fields": avro_schema_fields}
        logging.info(avro_schema)
        schema = avro.schema.parse(json.dumps(avro_schema))
        avro_file = os.path.join(self.avro_path, str(int(time.time() * 1000)) + ".avro")
        self.avro_writer = DataFileWriter(open(avro_file, "wb"), DatumWriter(), schema)

    def storage(self, json_data):
        if not json_data:
            return

        # 判断文件是否写满 放置到锁同步中 防止产生空文件
        try:
            self.storage_lock.acquire()
            # 创建文件
            if self.current_counter == 0:
                self.set_avro_writer(json_data)

            # 如果文件数量大于最大数量 则重新生成文件
            if self.current_counter >= self.file_counter:
                self.avro_writer.close()
                self.set_avro_writer(json_data)
                self.current_counter = 0

            logging.info(json.dumps(json_data, ensure_ascii=False))
            self.avro_writer.append(json_data)
            self.current_counter += 1
        except Exception as ex:
            traceback.print_exc()
        finally:
            self.storage_lock.release()
