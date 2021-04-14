"""
Date: 2021.3.22
Author: Justin

要点说明：
Map 地图
分多个系列填充颜色
"""

from pyecharts.faker import Faker
from pyecharts import options as opts
from pyecharts.charts import Map
from pyecharts.globals import ChartType, SymbolType
   

c = (
    Map()
    .add("商家A", 
         [('Russia',33),('China',199),('France',66)], 
         maptype="world",
         is_map_symbol_show=False, # 不描点
    )
    .add("商家B", 
         [('United States',99),('Brazil',155),('Egypt',11)], 
         maptype="world",
         is_map_symbol_show=True,
    )
    .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
    .set_global_opts(
        title_opts=opts.TitleOpts(title="Map-世界地图"),
        visualmap_opts=opts.VisualMapOpts(max_=200),
    )
)

c.render('./output/map_series.html')