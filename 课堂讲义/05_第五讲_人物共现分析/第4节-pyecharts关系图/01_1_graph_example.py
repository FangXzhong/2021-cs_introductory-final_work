"""
Date: 2020.03.12
Author: Justin

要点说明：
用第三方库pyecharts绘制关系图（Graph）
设计少量节点和连接，作为示例
"""

from pyecharts import options as opts
from pyecharts.charts import Graph

# Graph:关系图。图中包括节点（node）和连线（link）

# 节点列表
nodes = [ # name:节点名称, value:节点值, symbol_size:节点图标尺寸
    opts.GraphNode(name="点1", value=30, symbol_size=30),
    opts.GraphNode(name="点2", value=10, symbol_size=10),
    opts.GraphNode(name="点3", value=10, symbol_size=10),
    opts.GraphNode(name="点4", value=30, symbol_size=30),
    opts.GraphNode(name="点5", value=50, symbol_size=50),
]
# 连线列表
links = [ # source:连线起点, target:连线终点, value:连线的值，和图中线的长度有关
    opts.GraphLink(source="点1", target="点5", value=20000),
    opts.GraphLink(source="点2", target="点5", value=10000),
    opts.GraphLink(source="点3", target="点5", value=5000),
    opts.GraphLink(source="点4", target="点5", value=1000),
#    opts.GraphLink(source="结点4", target="结点1", value=10000),
]

# 生成一个空白的关系图对象
c = Graph()  
# 添加节点nodes和连线links，边长范围edge_length，节点间的互斥力repulsion
c.add("", nodes, links, edge_length=[10,100], repulsion=1000)
# 添加图的标题
c.set_global_opts(title_opts=opts.TitleOpts(title="关系图-示例"))

# 画图，生成本地 HTML 文件。默认会在当前目录生成 render.html 文件
# 也可以指定文件名，作为参数传入 
c.render('./output/关系图-示例.html')
