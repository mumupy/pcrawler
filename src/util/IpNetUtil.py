#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/8/15 21:21
# @Author  : ganliang
# @File    : IpNetUtil.py
# @Desc    : ip.net城市信息查询
import os

import datx
from src.config.Config import logging
BASE_DIR = os.path.dirname(os.path.dirname(os.getcwd())).replace("\\", "/")
IP_NET_DATA_PATH = BASE_DIR + "/data/ipdata/17monipdb.datx"


def query_city(ip):
    """查询地级市精度的IP库"""
    c = datx.City(IP_NET_DATA_PATH)
    logging.info(c.find("8.8.8.258"))
    logging.info(c.find("120.77.13.93"))


def query_district(ip):
    """查询国内区县库"""
    d = datx.District(IP_NET_DATA_PATH)
    logging.info(d.find("123.121.117.72"))


def query_baseStation(ip):
    """查询基站IP库"""
    d = datx.BaseStation(IP_NET_DATA_PATH)
    logging.info(d.find("223.221.121.0"))


if __name__ == "__main__":
    query_city("")
