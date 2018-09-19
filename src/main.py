#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/8/1 21:08
# @Author  : ganliang
# @File    : Crawler.py
# @Desc    : 爬虫核心入口

from src.config.Config import logging
from src.core.Crawler import Crawler
from src.processor.builtin.ImagePageProcess import ImagePageProcess
from src.processor.builtin.SinaNewsPageProcessor import SinaNewsPageProcessor
from src.processor.builtin.VedioPageProcess import VedioPageProcess
from src.processor.loophole.NsfocusLoopholePageProcess import NsfocusLoopholePageProcess
from src.scheduler.duplicate.BloomFilterDuplicateRemover import BloomFilterDuplicateRemover
from src.scheduler.duplicate.HashSetDuplicateRemover import HashSetDuplicateRemover
from src.storage.AvroStorage import AvroStorage
from src.storage.ConsoleStorage import ConsoleStorage
from src.storage.JsonStorage import JsonStorage
from src.storage.MediaStorage import MediaStorage


def crawler_news(url, outpath, thread_count=10, storage="json", duplicateRemover="bloom"):
    """爬取新浪湖北新闻数据

    url
        爬取的新闻网站地址,http://hb.sina.com.cn/news/
    outpath
        输出文件目录
    thread_count
        爬虫线程数量
    storage
       存储文件格式，默认为json
    duplicateRemover
        去除重复的方法，默认为bloom
    """
    if not url or not outpath:
        logging.error("url[%s] or outpath[%s] is empty!" % (url, outpath))
        return

    Crawler(url, SinaNewsPageProcessor()) \
        .set_thread(thread_count) \
        .set_storage(__get_storage__(storage, outpath)) \
        .set_duplicate_remover(__get_duplicate_remover__(duplicateRemover)) \
        .run()


def crawler_images(url, outpath, thread_count=10, storage="json", duplicateRemover="bloom"):
    """爬取网站图片资源
        url
            爬取的图片地址
        outpath
            输出文件目录
        thread_count
            爬虫线程数量
        duplicateRemover
            去除重复的方法，默认为bloom
        """
    if not url or not outpath:
        logging.error("url[%s] or outpath[%s] is empty!" % (url, outpath))
        return

    Crawler(url, ImagePageProcess()) \
        .set_thread(thread_count) \
        .set_storage(MediaStorage(outpath)) \
        .set_duplicate_remover(__get_duplicate_remover__(duplicateRemover)) \
        .run()

def crawler_video(url, outpath, thread_count=10, duplicateRemover="bloom"):
    """爬取多媒体视频
        url
            爬取的多媒体地址
        outpath
            输出文件目录
        thread_count
            爬虫线程数量
        duplicateRemover
            去除重复的方法，默认为bloom
        """
    if not url or not outpath:
        logging.error("url[%s] or outpath[%s] is empty!" % (url, outpath))
        return
    Crawler(url, VedioPageProcess()) \
        .set_thread(thread_count) \
        .set_storage(MediaStorage(outpath)) \
        .set_duplicate_remover(__get_duplicate_remover__(duplicateRemover)) \
        .run()


def crawler_nsfocus_loophole(outpath, thread_count=10, storage="json", duplicateRemover="bloom"):
    """绿盟漏洞爬取 http://www.nsfocus.net/index.php?act=sec_bug
        outpath
            输出文件目录
        thread_count
            爬虫线程数量
        storage
           存储方式 默认json
        duplicateRemover
            去除重复的方法，默认为bloom
        """
    if not outpath:
        logging.error("outpath[%s] is empty!" % outpath)
        return
    Crawler("http://www.nsfocus.net/index.php?act=sec_bug",
            NsfocusLoopholePageProcess(),
            filter_url=["http://www.nsfocus.net/index.php?act=sec_bug", "http://www.nsfocus.net/vulndb"]) \
        .set_thread(thread_count) \
        .set_storage(__get_storage__(storage, outpath)) \
        .set_duplicate_remover(__get_duplicate_remover__(duplicateRemover)) \
        .run()


def __get_storage__(storage, outpath):
    storage = storage.lower()
    if storage == "json":
        fileStorage = JsonStorage(outpath)
    elif storage == "avro":
        fileStorage = AvroStorage(outpath)
    elif storage == "console":
        fileStorage = ConsoleStorage()
    else:
        raise Exception("not support file storage [%s]" % storage)
    return fileStorage


def __get_duplicate_remover__(duplicateRemover):
    duplicateRemover = duplicateRemover.lower()
    if duplicateRemover == "bloom":
        duplicater = BloomFilterDuplicateRemover()
    elif duplicateRemover == "hashset":
        duplicater = HashSetDuplicateRemover()
    else:
        raise Exception("not support file duplicateRemover [%s]" % duplicateRemover)
    return duplicater
