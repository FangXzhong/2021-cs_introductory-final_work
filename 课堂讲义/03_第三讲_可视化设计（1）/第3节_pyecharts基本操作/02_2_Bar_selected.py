# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 20:14:11 2020
@author: Justin
"""
'''
Bar-默认取消显示某 Series
配置add_yaxis函数的参数
来自pyecharts 官方文档
'''

from pyecharts.faker import Faker
from pyecharts import options as opts
from pyecharts.charts import Bar

c = (
    Bar()
    .add_xaxis(Faker.choose())
    .add_yaxis("商家A", Faker.values())
    .add_yaxis("商家B", Faker.values(), is_selected=False) # 是否默认显示
    .set_global_opts(title_opts=opts.TitleOpts(title="Bar-默认取消显示某 Series"))
    .render("./output/bar_is_selected.html")
)
