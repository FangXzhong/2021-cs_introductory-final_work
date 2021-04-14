# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 16:56:34 2020
@author: Justin
"""
'''
Bar-自定义柱形的颜色
配置add_yaxis函数的color参数。优点是方便，缺点是有时会出现颜色错位
更好的方法是使用“系列配置项”中的“ItemStyleOpts：图元样式配置项”
https://pyecharts.org/#/zh-cn/series_options
'''

from pyecharts import options as opts
from pyecharts.faker import Faker
from pyecharts.charts import Bar

c = (
    Bar()
    .add_xaxis(Faker.choose())
    .add_yaxis("商家A", 
               Faker.values(),
               color='green', # 设置颜色
               )
    .add_yaxis("商家B", 
               Faker.values(),
               color='orange', # 设置颜色
               )
    .add_yaxis("商家C", 
               Faker.values(),
               color='darkblue', # 设置颜色
               )
    .set_global_opts(title_opts=opts.TitleOpts(title="Bar-自定义颜色"))
    .render("./output/bar_color.html")
)
 