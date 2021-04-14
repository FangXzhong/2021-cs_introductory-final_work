"""
Date: 2021.3.22
Author: Justin

要点说明：
绘制轮播柱形图
"""

from pyecharts.faker import Faker
from pyecharts import options as opts
from pyecharts.charts import Bar, Page, Pie, Timeline


x = Faker.choose()
tl = Timeline()
for i in range(2015, 2020):
    bar = (
        Bar()
        .add_xaxis(x)
        .add_yaxis("商家A", Faker.values())
        .add_yaxis("商家B", Faker.values())
        .set_global_opts(title_opts=opts.TitleOpts("某商店{}年营业额".format(i)))
    )
    tl.add(bar, "{}年".format(i))

tl.render('./output/timeline_bar.html')


    