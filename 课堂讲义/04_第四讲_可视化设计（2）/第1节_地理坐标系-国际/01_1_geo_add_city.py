"""
Date: 2021.3.22
Author: Justin

要点说明：
Geo 地理坐标系。
在地图上添加一个坐标点，以经纬度标记
"""

from pyecharts import options as opts
from pyecharts.charts import Geo
from pyecharts.globals import ChartType, SymbolType, GeoType

geo = Geo()

# 新增坐标点的函数，添加名称跟经纬度
# add_coordinate(
#    name: str, # 坐标地点名称
#    longitude: Numeric, # 经度
#    latitude: Numeric, # 纬度
# )

# 可以在网上查找城市的经纬度，然后根据经纬度在地图库中添加坐标点
geo.add_coordinate(
    name="Los Angeles",
    longitude=-118.15, 
    latitude=34.04
    )


# 在地图上添加坐标点，包括刚才新增的坐标点
geo.add("",
        [("Los Angeles",90),("北京",10)], 
        type_=ChartType.EFFECT_SCATTER
        )


# 添加数据项（即设置全图的范围）
geo.add_schema(maptype="world")

# 设置相关属性
geo.set_series_opts(label_opts=opts.LabelOpts(is_show=False))
geo.set_global_opts(visualmap_opts=opts.VisualMapOpts(max_=100),
                    title_opts=opts.TitleOpts(title="geo_add"))

# 输出到网页文件
geo.render('./output/geo_add_city.html')