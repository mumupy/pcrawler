Installation
============

使用pcrawler需要安装的组件。其中有些组件是程序需要的，而有些组件是为了编写文档和测试代码覆盖率而添加的
组件。

项目组件
--------
.. code :: python

    #使用bloomFilter来进行数据去重
    pip install pybloom

    #分析html
    pip install lxml

    #使用avro来存储爬虫数据
    pip install avro

其他组件
--------
.. code :: python

    #使用codecov来生成测试代码覆盖率
    pip install codecov

    #使用recommonmark来将md文件转化为rst文档
    pip install recommonmark