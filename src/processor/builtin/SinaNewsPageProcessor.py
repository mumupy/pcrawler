#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/8/13 19:50
# @Author  : ganliang
# @File    : SinaNewsPageProcessor.py
# @Desc    : 新浪新闻数据爬取
import time
import traceback

from lxml import etree

from src.config.Config import logging
from src.processor.PageProcess import PageProcess
from src.util.ElementUtil import *


class SinaNewsPageProcessor(PageProcess):
    """爬去新浪新闻数据"""

    def process(self, page):
        """处理一个页面 将页面的种子url添加到页面调度器中，同时对页面内容进行爬取"""
        res_html = self.handler(page)
        # 爬去新闻内容
        article_dict = self.fetchArticle(res_html)
        # 如果文件内容不存在 则过滤该数据
        if self.filter(page, article_dict):
            return
        article_dict.setdefault("url",page.url)
        article_dict.setdefault("create_time", time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time())))
        article_dict.setdefault("_id", abs(hash(page.url)))
        page.put_field_dict(article_dict)

    def filter(self, page, article_dict):
        """爬去的内容是否过滤"""
        if not article_dict.get("article_content"):
            page.is_filter = True
            return True
        return False

    def fetchArticle(self, html):
        """抓取页面内容"""
        article_dict = {}
        article_dict.update(self.fetchArticleContent(html))
        article_dict.update(self.fetchArticleHeader(html))
        article_dict.update(self.fetchArticleMeta(html))
        return article_dict

    def fetchArticleContent(self, html):
        # 抓取文本内容
        article_content_dict = {}
        try:
            article_content_elements = html.xpath("//div[@class='article-body main-body']/p")
            if not article_content_elements:
                article_content_elements = html.xpath("//div[@class='newsContent']/span[@id='newsCon']/p")
            if not article_content_elements:
                article_content_elements = html.xpath("//div[@class='main-body']/p")
            if not article_content_elements:
                article_content_elements = html.xpath("//div[@id='artibody']/p")

            article_contents = ""
            for article_content_element in article_content_elements:
                article_content = etree.tostring(article_content_element, encoding="UTF-8", pretty_print=False,
                                                 method="html")
                article_contents = article_contents + article_content
            article_content_dict.setdefault("article_content", article_contents)
            article_content_dict.setdefault("article_content_size", len(article_contents))
        except Exception as ex:
            logging.error(ex)
            traceback.print_exc()
        return article_content_dict

    def fetchArticleHeader(self, html):
        """获取文章头信息"""
        article_header_dict = {}
        try:
            article_header_elements = html.xpath("//div[@class='article-header clearfix']")
            if article_header_elements:
                article_header_element = article_header_elements[0]
                # 获取标题
                article_title = getElement(article_header_element, "//h1/text()")
                article_header_dict.setdefault("article_title", article_title)
                # 新闻发布时间
                source_time = getElement(article_header_element, "//p[@class='source-time']/span[1]/text()")
                article_header_dict.setdefault("source_time", source_time)
                # 新闻来源
                art_source = getElement(article_header_element,
                                        "//p[@class='source-time']/span[2]/span[@id='art_source']/text()")
                article_header_dict.setdefault("art_source", art_source)
                # 评论数量
                mcom_num = getElement(article_header_element, "//p[@class='source-time']/span[3]/a/b/@data-comment")
                article_header_dict.setdefault("mcom_num", mcom_num)
            else:
                article_title = html.xpath("//div[@class='newsContent']/h2[@class='news_tit']/text()")
                if article_title:
                    article_header_dict.setdefault("article_title", article_title[0])
                source_time = html.xpath("//div[@class='newsContent']/div[@class='artInfo']/text()")
                if source_time:
                    article_header_dict.setdefault("source_time", source_time[0])
                art_source = html.xpath("//div[@class='newsContent']/div[@class='artInfo']/a/text()")
                if art_source:
                    article_header_dict.setdefault("art_source", art_source[0])
                mcom_num = html.xpath("//em[@id='plcount']/text()")
                if mcom_num:
                    article_header_dict.setdefault("mcom_num", mcom_num[0])
        except Exception as ex:
            logging.error(ex)
            traceback.print_exc()
        return article_header_dict

    def fetchArticleMeta(self, html):
        """获取页面元数据"""
        article_meta_dict = {}
        try:
            # 消息类型
            meta_og_type = getElement(html, "//meta[@property='og:type']/@content")
            article_meta_dict.setdefault("meta_og_type", meta_og_type)
            # meta设置标题
            meta_og_title = getElement(html, "//meta[@property='og:title']/@content")
            article_meta_dict.setdefault("meta_og_title", meta_og_title)
            # meta设置内容
            meta_og_description = getElement(html, "//meta[@property='og:description']/@content")
            article_meta_dict.setdefault("meta_og_description", meta_og_description)
            # meta设置url地址
            meta_og_url = getElement(html, "//meta[@property='og:url']/@content")
            article_meta_dict.setdefault("meta_og_url", meta_og_url)
            # meta时间
            meta_og_create = getElement(html, "//meta[@property='weibo: article:create_at']/@content")
            article_meta_dict.setdefault("meta_og_create", meta_og_create)
            # 文本描述
            meta_keywords = getElement(html, "//meta[@name='Keywords']/@content")
            article_meta_dict.setdefault("meta_keywords", meta_keywords)
            # 文本描述
            meta_description = getElement(html, "//meta[@name='Description']/@content")
            article_meta_dict.setdefault("meta_description", meta_description)
            # 文本描述
            meta_tags = getElement(html, "//meta[@name='tags']/@content")
            article_meta_dict.setdefault("meta_tags", meta_tags)
        except Exception as ex:
            logging.error(ex)
            traceback.print_exc()
        return article_meta_dict

    def fetchArticleRecommand(self, html):
        """抓取页面推荐的消息内容"""
        pass

    def fetchArticleComment(self, html):
        """抓取页面评论数据"""
        pass
