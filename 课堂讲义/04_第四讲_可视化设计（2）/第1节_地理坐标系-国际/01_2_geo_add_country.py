"""
Date: 2021.3.22
Author: Justin

要点说明：
Geo 地理坐标系。
在地图上添加多个坐标点，以经纬度标记
设置坐标点之间的连线
"""

from pyecharts import options as opts
from pyecharts.charts import Geo
from pyecharts.globals import ChartType, SymbolType, GeoType

geo = Geo()

# 向“坐标库”中添加一个城市的坐标点
geo.add_coordinate(name="Los Angeles",longitude=-118.15, latitude=34.04)

# 向“坐标库”中添加若干国家的坐标点
# 注意：Geo中实质上只有坐标点的概念，这里用国家的地理中心的经纬度指代该国
geo.add_coordinate(name="Brazil",longitude=-51.925,latitude=-14.235)
geo.add_coordinate(name="Russia",longitude=37.618,latitude=55.751)
geo.add_coordinate(name="India",longitude=78.962,latitude=20.593)
geo.add_coordinate(name="China",longitude=104.195,latitude=35.675)
geo.add_coordinate(name="South Africa",longitude=22.937,latitude=-30.559)
geo.add_coordinate(name="Australia",longitude=133.775,latitude=-25.274)
geo.add_coordinate(name="Canada",longitude=-106.346,latitude=56.130)

# 添加数据项（设置地图范围）
geo.add_schema(maptype="world")

# 在地图上绘制坐标点
geo.add("",[("Los Angeles",80)], type_=ChartType.SCATTER)

geo.add("",
        [   ("Brazil",10),
            ("Russia",70),
            ("India",80),
            ("China",90),
            ("South Africa",80),
            ("Australia",50),
            ("Canada",20),
        ],
        type_=ChartType.EFFECT_SCATTER)

# 在地图上绘制流向
geo.add("全球走向",
        [   ("Australia","China"),
            ("Brazil","China"),
            ("South Africa","India"),
            ("India","China"),
            ("Russia","China"),
            ("Canada","Russia"),
            ("Los Angeles","China"),
        ],
        type_= GeoType.LINES,
        effect_opts=opts.EffectOpts(symbol=SymbolType.ARROW,
                                    symbol_size=5,color="yellow"),
        linestyle_opts=opts.LineStyleOpts(curve=0.2),
       )

# 设置相关属性
geo.set_series_opts(label_opts=opts.LabelOpts(is_show=False))
geo.set_global_opts(visualmap_opts=opts.VisualMapOpts(max_=100),
                    title_opts=opts.TitleOpts(title="geo_add"))

# 输出到网页文件
geo.render('./output/geo_add_country.html')