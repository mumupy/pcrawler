#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/8/12 22:01
# @Author  : ganliang
# @File    : Install.py
# @Desc    : 安装器
import os
import sys

from src.config.Config import logging


def install():
    os.system("pip install lxml")  # 解析html
    os.system("pip install pybloom")  # bloomfilter布隆过滤器
    os.system("pip install chardet")  # 自动识别字符串编码格式
    os.system("pip install ipip-datx")  # ipipnet的ip数据解析
    os.system("pip install avro")  # avro数据存储格式


def sitecustomize():
    for sys_path in sys.path:
        if sys_path.endswith("site-packages"):
            logging.info(sys_path)
            sitecustomize_path = os.path.join(sys_path, "sitecustomize.py")
            if not os.path.exists(sitecustomize_path):
                sitecustomize_file = open(sitecustomize_path, "w")
                sitecustomize_file.write("#!/usr/bin/env python\n")
                sitecustomize_file.write("# -*- coding: utf-8 -*-\n")
                sitecustomize_file.write("# @Time    : 2018/8/9 23:55\n")
                sitecustomize_file.write("# @Author  : ganliang\n")
                sitecustomize_file.write("# @File    : sitecustomize.py\n")
                sitecustomize_file.write("# @Desc    : 解决乱码问题\n")
                sitecustomize_file.write("import sys\n")
                sitecustomize_file.write("reload(sys)\n")
                sitecustomize_file.write("sys.setdefaultencoding('utf8')\n")
                sitecustomize_file.close()
                logging.info("write {0} sitecustomize.py success".format(sitecustomize_path))
                break
            else:
                logging.info("sitecustomize.py exists")


if __name__ == "__main__":
    install()
    sitecustomize()
