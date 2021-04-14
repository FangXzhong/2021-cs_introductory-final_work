# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 12:47:21 2020
@author: Justin
"""
'''
Bar-显示水平方向的缩放滑块
通过配置set_global_opts函数的参数实现

详见“全局配置项”中的“DataZoomOpts：区域缩放配置项”
https://pyecharts.org/#/zh-cn/global_options?id=datazoomopts%EF%BC%9A%E5%8C%BA%E5%9F%9F%E7%BC%A9%E6%94%BE%E9%85%8D%E7%BD%AE%E9%A1%B9

来自pyecharts 官方文档
'''
from pyecharts import options as opts
from pyecharts.charts import Bar
from pyecharts.faker import Faker

c = (
    Bar()
    .add_xaxis(Faker.days_attrs)
    .add_yaxis("商家A", Faker.days_values)
    .set_global_opts(
        title_opts=opts.TitleOpts(title="Bar-DataZoom（slider-水平）"),
        datazoom_opts=opts.DataZoomOpts(),
    )
    .render("./output/bar_datazoom_slider.html")
)