# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 16:56:34 2020
@author: Justin
"""
'''
Bar-自定义柱形的多个系列配置项
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
               label_opts=opts.LabelOpts(position='insideBottom'), # 设置标签位置
               )
    .add_yaxis("商家B", 
               Faker.values(),
               itemstyle_opts=opts.ItemStyleOpts(color='orange'), # 设置颜色
               label_opts=opts.LabelOpts(position='insideTop',font_size=20), # 设置标签位置和字号
               )
    .add_yaxis("商家C", 
               Faker.values(),
               itemstyle_opts=opts.ItemStyleOpts(color='darkblue'), # 设置颜色
               )
    .set_global_opts(title_opts=opts.TitleOpts(title="Bar-自定义多个系列配置项"))
    .render("./output/bar_label_opts.html")
)
 