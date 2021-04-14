# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 20:39:22 2020
@author: Justin
"""
'''
Geo 地理坐标系 - 一省地图 + 热力图
来自pyecharts 官方文档
'''
from pyecharts import options as opts
from pyecharts.charts import Geo
from pyecharts.faker import Faker
from pyecharts.globals import ChartType

c = (
    Geo()
    .add_schema(maptype="广东")
    .add(
        "geo",
        [list(z) for z in zip(Faker.guangdong_city, Faker.values())],
        type_=ChartType.HEATMAP,
    )
    .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
    .set_global_opts(
        visualmap_opts=opts.VisualMapOpts(range_color=Faker.visual_color), 
        title_opts=opts.TitleOpts(title="Geo-广东地图")
    )
    .render("./output/geo_guangdong.html")
)