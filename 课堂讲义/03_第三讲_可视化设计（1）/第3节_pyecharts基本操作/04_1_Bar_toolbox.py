# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 20:30:27 2020
@author: Justin
"""
'''
Bar-显示 ToolBox
通过配置set_global_opts函数的参数实现
详见“全局配置项”中的“ToolboxOpts：工具箱配置项”和“LegendOpts：图例配置项”

来自pyecharts 官方文档
'''

from pyecharts.faker import Faker
from pyecharts import options as opts
from pyecharts.charts import Bar

c = (
    Bar()
    .add_xaxis(Faker.choose())
    .add_yaxis("商家A", Faker.values())
    .add_yaxis("商家B", Faker.values())
    .set_global_opts(
        title_opts=opts.TitleOpts(title="Bar-显示 ToolBox"),
        toolbox_opts=opts.ToolboxOpts(), # 显示工具栏
        legend_opts=opts.LegendOpts(is_show=False) #是否显示图例
    )
    .render("./output/bar_toolbox.html")
)
 