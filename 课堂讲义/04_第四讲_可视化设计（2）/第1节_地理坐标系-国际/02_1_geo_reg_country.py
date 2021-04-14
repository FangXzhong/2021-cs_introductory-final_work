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

register_url("https://echarts-maps.github.io/echarts-countries-js/")
## 上面这行语句会去网上加载地图，需要联网
## 可以登录该网址查看有哪些国家
## 如果运行时出现 ssl 异常，则在本程序开始处添加下面两行代码
# import ssl
# ssl._create_default_https_context = ssl._create_unverified_context

#----------------------------------------------
## 指定某一国地图
site_name = "巴西"  # 瑞士，美国，德国，巴西，俄罗斯，……
geo = (
    Geo()
    .add_schema(maptype=site_name)
    .set_global_opts(title_opts=opts.TitleOpts(title=site_name))
)
# 如果有该国的坐标点，则可以在图上绘制坐标点

geo.render('./output/geo_reg_{}.html'.format(site_name))
