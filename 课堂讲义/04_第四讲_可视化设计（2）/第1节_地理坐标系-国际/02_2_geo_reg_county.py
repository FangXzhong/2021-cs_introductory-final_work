"""
Date: 2021.3.22
Author: Justin

要点说明：
Geo 地理坐标系。从官网加载新的区域地图
参考pyecharts 官方文档
"""

from pyecharts import options as opts
from pyecharts.charts import Geo
from pyecharts.datasets import register_url

# 如果出现 ssl 异常的话加上下面两行代码
# import ssl
# ssl._create_default_https_context = ssl._create_unverified_context


#----------------------------------------------
## 获取中国县级行政区划的地图，可以登录下面的网址查看有哪些县
register_url("https://echarts-maps.github.io/echarts-china-counties-js/")

county = '海淀区'  # 海淀区，东城区，浦东新区，……
geo = (
    Geo()
    .add_schema(maptype=county)
    .set_global_opts(title_opts=opts.TitleOpts(title=county))
)

geo.render('./output/geo_reg_{}.html'.format(county))
