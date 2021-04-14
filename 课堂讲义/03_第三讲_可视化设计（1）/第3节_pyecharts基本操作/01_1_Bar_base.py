# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 20:01:20 2020
@author: Justin
"""
'''
Bar-基本示例，来自pyecharts 官方文档：
https://pyecharts.org/#/zh-cn/intro

学会阅读“链式调用”，只需要能读懂，不用会写。因为pyecharts官网的示例都用这种格式
学会阅读官网的函数定义和示例
'''

from pyecharts import options as opts
from pyecharts.charts import Bar
from pyecharts.faker import Faker


c = (
    Bar()
    .add_xaxis(Faker.choose())
    .add_yaxis("商家A", Faker.values())
    .add_yaxis("商家B", Faker.values())
    .set_global_opts(title_opts=opts.TitleOpts(title="Bar-基本示例", subtitle="我是副标题"))
    .render("bar_base.html")
)


# ---上面的链式调用和下面的代码功能相同
c = Bar()
c.add_xaxis(Faker.choose())
c.add_yaxis("商家A", Faker.values())
c.add_yaxis("商家B", Faker.values())
c.set_global_opts(title_opts=opts.TitleOpts(title="Bar-基本示例", subtitle="我是副标题"))
c.render("./output/bar_base.html")
