# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 20:31:52 2020
@author: Justin
"""
'''
Geo 地理坐标系 - 基本图
参考pyecharts 官方文档
'''
from pyecharts import options as opts
from pyecharts.charts import Geo
from pyecharts.faker import Faker

c = (
    Geo()
        .add_schema(maptype="china")
        #    .add("geo", [list(z) for z in zip(Faker.provinces, Faker.values())])
        .add('geo',
             [("北京", 10), ("上海", 30),
              ("广东", 50), ("陕西", 70),
              ("乌鲁木齐", 90)],
             # 省市标记参数是由元组项组成的列表，图上标记的颜色和数值有关
             )
        .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
        .set_global_opts(
        visualmap_opts=opts.VisualMapOpts(),
        title_opts=opts.TitleOpts(title="Geo-基本示例")
    )
        .render("./output/geo_base.html")
)
