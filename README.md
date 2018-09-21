# pcrawler爬虫程序
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://github.com/mumupy/pcrawler/blob/master/LICENSE)
[![Build Status](https://travis-ci.org/mumupy/pcrawler.svg?branch=master)](https://travis-ci.org/mumupy/pcrawler)
[![codecov](https://codecov.io/gh/mumupy/pcrawler/branch/master/graph/badge.svg)](https://codecov.io/gh/mumupy/pcrawler)
[![pypi](https://img.shields.io/pypi/v/pcrawler.svg)](https://pypi.python.org/pypi/pcrawler)
[![readthedocs](https://readthedocs.org/projects/pcrawler/badge/?version=latest)](https://pcrawler.readthedocs.io)  

***pcrawler是一款python版本的爬虫程序，通过该爬虫程序可以非常快速方便的编写一个自己的爬虫程序。pcrawler主要
包含downloader、schedular、processor、storage四大组件组成。而且可以非常方便快捷的拓展各个组件。***

## 特性：
- 简单的API，可快速上手
- 模块化的结构，可轻松扩展
- 提供多线程和分布式支持

## 架构
pcrawler主要包含downloader、schedular、processor、storage四大组件组成。
- processor 爬虫页面处理器，对页面进行分析。目前集成图片下载处理器、多媒体视频下载处理器、新浪新闻处理器。
- schedular URL管理组件，对待抓取的URL队列进行管理，对已抓取的URL进行去重。目前url队列管理支持文件缓存管理和集合管理。url去重支持文件缓存、集合、bloomFilter布隆过滤器等。
- downloader 下载组件，默认使用urllib2下载。
- storage 存储组件，支持多样文件格式(csv、json、avro、video)

## 相关阅读  
[webmagic爬虫](http://webmagic.io/)  
[Bloom Filter](http://blog.csdn.net/jiaomeng/article/details/1495500)

## 联系方式
**以上观点纯属个人看法，如有不同，欢迎指正。  
email:<babymm@aliyun.com>  
github:[https://github.com/babymm](https://github.com/babymm)**
