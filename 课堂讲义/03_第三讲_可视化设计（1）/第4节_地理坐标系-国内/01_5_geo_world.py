# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 23:59:08 2020
@author: Justin
"""
'''
Geo 地理坐标系。世界地图
参考pyecharts 官方文档
'''
from pyecharts.faker import Faker
from pyecharts import options as opts
from pyecharts.charts import Geo
from pyecharts.globals import ChartType, SymbolType

c = (
    Geo()
    .add_schema(maptype="world")
    .add(
        "geo",
        #[list(z) for z in zip(Faker.provinces, Faker.values())],
        [('北京',33), ('新疆',99), ('伦敦',66)],
        # 只能调用国内省市，本地库中没有国外城市数据。可以手工添加或网上获取
        type_=ChartType.EFFECT_SCATTER,
    )
    .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
    .set_global_opts(
        visualmap_opts=opts.VisualMapOpts(),
        title_opts=opts.TitleOpts(title="Geo-世界地图"),
    )
    
    .render('./output/geo_world.html')
)
