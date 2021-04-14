# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 16:56:34 2020
@author: Justin
"""
'''
Bar-自定义柱形的颜色
配置add_yaxis函数的参数
1）可以直接使用add_yaxis函数的color参数，有时会出现颜色错位
2）这里使用的是“系列配置项”中的“ItemStyleOpts：图元样式配置项”
https://pyecharts.org/#/zh-cn/series_options
'''

from pyecharts.faker import Faker
from pyecharts import options as opts
from pyecharts.charts import Bar

c = (
    Bar()
    .add_xaxis(Faker.choose())
    .add_yaxis("商家A", 
               Faker.values(),
               itemstyle_opts=opts.ItemStyleOpts(color='green'), # 设置颜色
               )
    .add_yaxis("商家B", 
               Faker.values(),
               itemstyle_opts=opts.ItemStyleOpts(color='orange'), # 设置颜色
               )
    .add_yaxis("商家C", 
               Faker.values(),
               itemstyle_opts=opts.ItemStyleOpts(color='darkblue'), # 设置颜色
               )
    .set_global_opts(title_opts=opts.TitleOpts(title="Bar-用系列配置项自定义颜色"))
    .render("./output/bar_color_opts.html")
)
 