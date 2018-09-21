#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/9/21 17:03
# @Author  : ganliang
# @File    : coverageUtil.py
# @Desc    : coverage代码测试覆盖率

import coverage

import crawler


def code_coverage():
    cov = coverage.coverage()
    cov.start()
    crawler.__crawler_travis__()
    cov.stop()
    cov.report()
    cov.html_report(directory="covhtml")


if __name__ == "__main__":
    code_coverage()
