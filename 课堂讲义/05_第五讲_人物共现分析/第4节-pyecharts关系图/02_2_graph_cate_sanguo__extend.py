"""
Date: 2020.03.12
Author: Justin

要点说明：
用第三方库pyecharts绘制关系图（Graph）,带分类节点
使用前面程序生成的三国人物关系数据
数据有手工调整，增加了分类信息
"""

from pyecharts import options as opts
from pyecharts.charts import Graph

##--- 第0步：准备工作
# 输入文件
#node_file_name = './data/三国演义-段落示例-人物节点.csv'
#link_file_name = './data/三国演义-段落示例-人物连接.csv'
node_file_name = './data/三国演义-人物节点-分类.csv' # 手工增加国别分类
link_file_name = './data/三国演义-人物连接.csv'
# 输出文件
out_file_name = './output/关系图-分类-三国人物.html'

##--- 第1步：从文件读入节点和连接信息
node_file = open(node_file_name, 'r')
node_line_list = node_file.readlines()
node_file.close()
del node_line_list[0]  # 删除标题行

link_file = open(link_file_name, 'r')
link_line_list = link_file.readlines()
link_file.close()
del link_line_list[0]  # 删除标题行

##--- 第2步：解析读入的信息，存入列表
# 类别列表，用于给节点分成不同系列，会自动用不同颜色表示
categories=[{}, {'name':'魏'}, {'name':'蜀'},{'name':'吴'},{'name':'群'}]

node_in_graph = []
for one_line in node_line_list:
    one_line = one_line.strip('\n')
    one_line_list = one_line.split(',')
    #print(one_line_list)  # 测试点
    node_in_graph.append(opts.GraphNode(
            name=one_line_list[0], 
            value=int(one_line_list[1]), 
            symbol_size=int(one_line_list[1])/20,  # 手动调整节点的尺寸
            category=int(one_line_list[2])))  # 类别，例如categories[2]=='蜀'
#print('-'*20)  # 测试点
link_in_graph = []
for one_line in link_line_list:
    one_line = one_line.strip('\n')
    one_line_list = one_line.split(',')
    #print(one_line_list)  # 测试点
    link_in_graph.append(opts.GraphLink(
            source=one_line_list[0], 
            target=one_line_list[1], 
            value=int(one_line_list[2])))


##--- 第3步：画图
c = Graph()
c.add("", 
      node_in_graph, 
      link_in_graph, 
      edge_length=[10,50], 
      repulsion=5000,
      categories=categories, 
#      linestyle_opts=opts.LineStyleOpts(curve=0.2),  # 增加连线弧度
      layout="force",  # "force"-力引导布局，"circular"-环形布局
      )
c.set_global_opts(title_opts=opts.TitleOpts(title="关系图-三国人物-分类"))
c.render(out_file_name)