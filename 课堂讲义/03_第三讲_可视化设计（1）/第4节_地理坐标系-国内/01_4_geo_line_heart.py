# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 22:39:18 2020
@author: Justin
"""
'''
Geo 地理坐标系。多点之间的连线
参考pyecharts 官方文档
'''
from pyecharts.faker import Faker
from pyecharts import options as opts
from pyecharts.charts import Geo
from pyecharts.globals import ChartType, SymbolType

c = (
    Geo()
        .add_schema(
        maptype="china",
        itemstyle_opts=opts.ItemStyleOpts(color="grey", border_color="black"), )
        .add(
        "",
        [("兰州", 1), ("银川", 1), ("石家庄", 1),
         ("徐州", 1), ("武汉", 1), ("长沙", 1), ("百色", 1), ("丽江", 1),
         ("林芝", 1), ("安多", 1), ("格尔木", 1), ("张掖", 1),
         ],
        # 城市标记参数是由元组项组成的列表
        type_=ChartType.SCATTER,
        itemstyle_opts=opts.ItemStyleOpts(color='white'),
    )
        .add(
        "",
        [("成都", 10)],
        # 城市标记参数是由元组项组成的列表
        type_=ChartType.EFFECT_SCATTER,
        # color="blue",
        itemstyle_opts=opts.ItemStyleOpts(color='red'),
    )
        .add(
        "我的",
        [("兰州", "银川"), ("银川", "石家庄"), ("石家庄", "济南"),
         ("济南", "徐州"), ("徐州", "武汉"), ("武汉", "长沙"), ("长沙", "百色"),
         ("百色", "丽江"), ("丽江", "林芝"), ("林芝", "安多"), ("安多", "格尔木"),
         ("格尔木", "张掖"), ("张掖", "兰州"), ],
        # 连线方向参数是由元组项组成的列表
        type_=ChartType.LINES,
        effect_opts=opts.EffectOpts(
            symbol=SymbolType.ARROW, symbol_size=6, color="white"
        ),
        linestyle_opts=opts.LineStyleOpts(curve=0.2),
        # curve为正时，曲线是凸的；为负时，曲线是凹的
        color='yellow',
    )
        #    .add(
        #        "你",
        #        [("兰州", "成都")],
        #         #连线方向参数是由元组项组成的列表
        #        type_=ChartType.LINES,
        #        effect_opts=opts.EffectOpts(
        #            symbol=SymbolType.ARROW, symbol_size=6, color="yellow"
        #        ),
        #        linestyle_opts=opts.LineStyleOpts(curve=0.2),
        #        # curve为正时，曲线是凸的；为负时，曲线是凹的
        #    )
        .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
        .set_global_opts(title_opts=opts.TitleOpts(title="Geo-Line-Heart"))

        .render('./output/geo_line_heart.html')
)
