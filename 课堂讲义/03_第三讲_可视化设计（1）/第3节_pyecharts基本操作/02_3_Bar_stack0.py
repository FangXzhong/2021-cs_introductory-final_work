# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 12:39:04 2020
@author: Justin
"""
'''
Bar-把多个Series的数据堆叠显示
配置add_yaxis函数的参数
来自pyecharts 官方文档
'''
from pyecharts import options as opts
from pyecharts.charts import Bar
from pyecharts.faker import Faker

c = (
    Bar()
    .add_xaxis(Faker.choose())
    .add_yaxis("商家A", Faker.values(), stack="stack0")
    .add_yaxis("商家B", Faker.values(), stack="stack0")
    .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
    .set_global_opts(title_opts=opts.TitleOpts(title="Bar-堆叠数据（全部）"))
    .render("./output/bar_stack0.html")
)