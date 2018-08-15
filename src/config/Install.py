#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/8/12 22:01
# @Author  : ganliang
# @File    : Install.py
# @Desc    : 安装器
import os
import sys


def install():
    os.system("pip install lxml")
    os.system("pip install pybloom")
    os.system("pip install chardet")


def sitecustomize():
    for sys_path in sys.path:
        if sys_path.find("site-packages") > -1:
            print(sys_path)
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
                print("write sitecustomize.py success")
            else:
                print("sitecustomize.py exists")


if __name__ == "__main__":
    sitecustomize()
