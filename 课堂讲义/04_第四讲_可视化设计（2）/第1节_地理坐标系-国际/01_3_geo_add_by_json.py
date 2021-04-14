"""
Date: 2021.3.22
Author: Justin

要点说明：
Geo 地理坐标系。批量添加坐标点，有两个方法：
1. 通过json格式的文件，批量添加坐标点
2. 把json格式的坐标信息添加到文件：pyecharts.datasets.city_coordinates.json
    即pyecharts安装目录下的./datasets/city_coordinates.json
    在命令行输入pip show pyecharts，可以查看pyecharts安装目录

上述第1种方法，仅对本程序有效。第2种方法，对本计算机上运行的程序都有效
"""

from pyecharts import options as opts
from pyecharts.charts import Geo
from pyecharts.globals import ChartType, SymbolType, GeoType

geo = Geo()

#----以JSON文件格式批量新增坐标点----
geo.add_coordinate_json(json_file='./data/world_country.json')

# 添加数据项
geo.add_schema(maptype="world")
geo.add("",
        [   ("Brazil",11),
            ("Russia",22),
            ("India",33),
            ("China",99),
            ("South Africa",44),
            ("New Zealand",55),
            ("Mexico",66),
         ],
         type_=ChartType.EFFECT_SCATTER
)

# 绘制流向
geo.add("全球走向",
        [   ("New Zealand","China"),
            ("Brazil","China"),
            ("South Africa","India"),
            ("India","China"),
            ("Russia","China"),
            ("Mexico","Russia"),
        ],
        type_= GeoType.LINES,
        effect_opts=opts.EffectOpts(symbol=SymbolType.ARROW,
                                    symbol_size=5,color="yellow"),
        linestyle_opts=opts.LineStyleOpts(curve=0.2),
)
        
geo.set_series_opts(label_opts=opts.LabelOpts(is_show=False))
geo.set_global_opts(visualmap_opts=opts.VisualMapOpts(max_=100),
                    title_opts=opts.TitleOpts(title="geo_add_json"))

geo.render('./output/geo_add_by_json.html')

