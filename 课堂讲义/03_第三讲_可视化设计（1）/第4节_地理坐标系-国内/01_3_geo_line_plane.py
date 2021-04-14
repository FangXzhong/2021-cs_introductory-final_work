# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 22:39:18 2020
@author: Justin
"""
'''
Geo 地理坐标系。多点之间的连线
参考pyecharts 官方文档
'''
from pyecharts.faker import Faker
from pyecharts import options as opts
from pyecharts.charts import Geo
from pyecharts.globals import ChartType, SymbolType


c = (
    Geo()
    .add_schema(
            maptype="china",
            itemstyle_opts=opts.ItemStyleOpts(color="grey", border_color="black"),)
    .add(
        "",
        [("广州", 50), ("北京", 60), ("杭州", 70), ("重庆", 80), ("乌鲁木齐", 90)],
         #城市标记参数是由元组项组成的列表
        type_=ChartType.EFFECT_SCATTER,
        color="white",
    )
    .add(
        "",
        [("漠河", 10), ("长沙", 10), ("拉萨", 10), ("西安", 20), ("重庆", 20), ("敦煌", 20),],
         #城市标记参数是由元组项组成的列表
        type_=ChartType.SCATTER,
        color="white",
    )
    .add(
        "国航",
        [("北京", "乌鲁木齐"), ("北京", "杭州"), ("北京", "漠河"),
         ("杭州", "长沙"), ("乌鲁木齐", "拉萨")],
         #连线方向参数是由元组项组成的列表
        type_=ChartType.LINES,
        effect_opts=opts.EffectOpts(
            symbol=SymbolType.ARROW, symbol_size=6, color="white"
        ),
        linestyle_opts=opts.LineStyleOpts(curve=0.2),
        # curve为正时，曲线是凸的；为负时，曲线是凹的
    )
    .add(
        "南航",
        [("广州", "重庆"), ("广州", "北京"), ("广州", "杭州"), 
         ("广州", "西安"), ("重庆", "敦煌")],
         #连线方向参数是由元组项组成的列表
        type_=ChartType.LINES,
        effect_opts=opts.EffectOpts(
            symbol=SymbolType.ARROW, symbol_size=6, color="yellow"
        ),
        linestyle_opts=opts.LineStyleOpts(curve=0.2),
        # curve为正时，曲线是凸的；为负时，曲线是凹的
    )
    .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
    .set_global_opts(title_opts=opts.TitleOpts(title="Geo-Line-Plane"))
    
    .render('./output/geo_line_plane.html')
)

