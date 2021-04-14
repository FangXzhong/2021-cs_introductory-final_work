"""
Date: 2021.3.22
Author: DEER

要点说明：
用geo画出全国人口图
"""

from pyecharts import options as opts
from pyecharts.charts import Geo
from pyecharts.globals import ChartType, SymbolType

# 2020年全国人口数据
data ={
"广东":11346,
"山东":10047,
"河南":9605,
"四川":8341,
"江苏":8051,
"河北":7556,
"湖南":6899,
"安徽":6324,
"湖北":5917,
"浙江":5737,
"广西":4926,
"云南":4830,
"江西":4648,
"辽宁":4359,
"福建":3941,
"陕西":3864,
"黑龙江":3773,
"山西":3718,
"贵州":3600,
"重庆":3102,
"吉林":2704,
"甘肃":2637,
"内蒙古":2491,
"新疆":2487,
"上海":2424,
"台湾":2359,
"北京":2154,
"天津":1560,
"海南":934,
"香港":745,
"宁夏":688,
"青海":603,
"西藏":335,
"澳门":63,
}

map_data = list(data.items()) 

c = (
    Geo() 
    .add_schema(map_type="china")
    .add("2020年人口（单位：万）", 
         map_data, 
         type_=ChartType.SCATTER,
         )
    .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
    .set_global_opts(
        visualmap_opts=opts.VisualMapOpts(max_=12000, is_piecewise=True),
        title_opts=opts.TitleOpts(title="各省人口数"),
    )
)

c.render("./output/全国人口数据地图_geo.html")  


