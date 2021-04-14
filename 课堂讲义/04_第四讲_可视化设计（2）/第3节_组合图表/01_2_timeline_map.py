"""
Date: 2021.3.22
Author: Justin

要点说明：
绘制轮播地图
"""

from pyecharts.faker import Faker
from pyecharts import options as opts
from pyecharts.charts import Bar, Page, Pie, Timeline
from pyecharts.charts import Map

#----------------------------------------------

tl = Timeline()

zone = [0,0,0,0,0]
zone[0] = [('浙江',99),('江苏',33)]
zone[1] = [('浙江',88),('上海',55),('安徽',77)]
zone[2] = [('上海',99),('安徽',77),('河南',88),('河北',55)]
zone[3] = [('安徽',77),('河南',44),('北京',22),('内蒙古',77)]
zone[4] = [('北京',22),('内蒙古',77),('陕西',11),('湖北',99),('西藏',66),('四川',33)]


for i in range(2016, 2021):
    map0 = (
        Map()
        .add("某商家重点市场", 
             zone[i-2016],
             maptype="china",
             is_map_symbol_show=False,  # 不描点
        )
        .set_global_opts(
            title_opts=opts.TitleOpts(title="Map-{}年市场情况".format(i)),
            visualmap_opts=opts.VisualMapOpts(max_=100),
        )
    )
    tl.add(map0, "{}年".format(i))
    
tl.render('./output/timeline_map.html')
    