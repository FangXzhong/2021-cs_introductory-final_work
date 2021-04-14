# -*- coding: utf-8 -*-
"""
Created on Mon Mar 29 11:29:33 2021

@author: DEER
"""

"""
Date: 2021.3.22
Author: Justin

要点说明：
绘制轮播地图，区域列表的另一种生成方式（逐渐扩大的区域）
"""

from pyecharts.faker import Faker
from pyecharts import options as opts
from pyecharts.charts import Bar, Page, Pie, Timeline
from pyecharts.charts import Map

#----------------------------------------------

tl = Timeline()

zone = []
zone.append([('浙江',99),('江苏',88),('上海',88)])
zone.append(zone[0] + [('安徽',77),('江西',66),('山东',77),('福建',66)])
zone.append(zone[1] + [('河南',44),('河北',55),('山西',44),('广东',44),('广西',55)])
zone.append(zone[2] + [('北京',22),('内蒙古',22),('陕西',33),('甘肃',33),('青海',33)])
zone.append(zone[3] + [('湖南',11),('湖北',1),('宁夏',11),('西藏',11),('四川',1)])

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
    
tl.render('./output/timeline_map2.html')
    