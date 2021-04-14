"""
Date: 2021.3.22
Author: Justin

要点说明：
Map 地图
在世界地图上填充区域色块

参考pyecharts 官方文档
"""

from pyecharts.faker import Faker
from pyecharts import options as opts
from pyecharts.charts import Map

# 注： map.add()函数中的maptype参数指明地图类型
# 具体参考 pyecharts.datasets.map_filenames.json 文件

c = (
    Map()
    .add("商家A", 
         [list(z) for z in zip(Faker.country, Faker.values())], 
         maptype="world",
         is_map_symbol_show=False,  # 不描点
    )
    .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
    .set_global_opts(
        title_opts=opts.TitleOpts(title="Map-世界地图"),
        visualmap_opts=opts.VisualMapOpts(max_=200, is_piecewise=True),
    )
)

c.render('./output/map_world.html')