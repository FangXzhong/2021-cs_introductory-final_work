# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 20:14:11 2020
@author: Justin
"""
'''
Bar-设置多个Series
配置add_yaxis函数的参数
'''

from pyecharts.faker import Faker
from pyecharts import options as opts
from pyecharts.charts import Bar

c = (
    Bar()
    .add_xaxis(Faker.choose())
    .add_yaxis("商家A", Faker.values())
    .add_yaxis("商家B", Faker.values()) # 第二组数据
    .add_yaxis("商家C", Faker.values()) # 第三组数据    
    .set_global_opts(title_opts=opts.TitleOpts(title="Bar-两组数据"))
    .render("./output/bar_multi_series.html")
)
