"""
Date: 2021.3.22
Author: Justin

要点说明：
Map 地图
在一省地图上填充区域色块

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
         [list(z) for z in zip(Faker.guangdong_city, Faker.values())], 
         maptype="广东",
    )
    .set_global_opts(
        title_opts=opts.TitleOpts(title="Map-VisualMap（分省分段型）"),
        visualmap_opts=opts.VisualMapOpts(max_=200, is_piecewise=True),
        is_piecewise=True 设置了分段色块
    )
)

c.render('./output/map_visual_prov.html')