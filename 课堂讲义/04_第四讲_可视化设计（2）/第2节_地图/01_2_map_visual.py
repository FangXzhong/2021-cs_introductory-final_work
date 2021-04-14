"""
Date: 2021.3.22
Author: Justin

要点说明：
Map 地图
在中国地图上填充区域色块

参考pyecharts 官方文档
"""

from pyecharts.faker import Faker
from pyecharts import options as opts
from pyecharts.charts import Map

# 注： map.add()函数中的maptype参数指明地图类型
# 具体参考 pyecharts.datasets.map_filenames.json 文件


## 用于绘图的数据，随机生成：
prov_list = [('广东', 98), ('北京', 125), ('上海', 134), 
             ('江西', 56), ('湖南', 136), ('浙江', 139), 
             ('江苏', 88)]

## 在中国地图上绘制上述数据，即填充对应省份的区域
c = (
    Map()
    .add("商家A", 
         prov_list, 
         maptype="china",
    )
    .set_global_opts(
        title_opts=opts.TitleOpts(title="Map-VisualMap（渐变型）"),
        visualmap_opts=opts.VisualMapOpts(max_=200),  # 此项配置渐变色的最大数值
    )
)

c.render('./output/map_visual.html')
