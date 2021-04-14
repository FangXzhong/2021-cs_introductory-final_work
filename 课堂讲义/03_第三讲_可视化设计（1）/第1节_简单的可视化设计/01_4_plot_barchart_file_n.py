# -*- coding: utf-8 -*-
"""
Created on Mon Mar 17 13:59:26 2021
@author: Deer
"""
'''
从文件读出数据后，绘制图表
'''

# import matplotlib
import matplotlib.pyplot as plt

# 指定所用中文的字体
import os

if os.name == "nt":  # Windows系统
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 设置字体
else:  # MacOS系统
    plt.rcParams["font.family"] = 'Arial Unicode MS'
plt.rcParams['axes.unicode_minus'] = False  # 支持负号的正常显示

src_filename = './短文-人物词频.csv'

src_file = open(src_filename, 'r')
line_list = src_file.readlines()
src_file.close()

print(line_list)

word_list = []
cnt_list = []

del line_list[0]  # 删除csv文件中的标题行

for line in line_list:
    line = line.replace('\n', '')
    word_cnt = line.split(',')
    word_list.append(word_cnt[0])
    cnt_list.append(int(word_cnt[1]))

print(word_list)
print(cnt_list)

# 绘制柱状图的另一种方式（分别设置x轴的刻度和标注）
n = len(cnt_list)
# 设置图的主体内容。两个参数分别是x轴和y轴的值
# 例如: range(4)是列表[0,1,2,3]，cnt_list是列表[5,3,2,2]
# 那下面函数要画的点是：(x=0,y=5),(x=1,y=3),(x=2,y=2),(x=3,y=2)
plt.bar(range(n), cnt_list[0:n])
# 设置x轴的刻度和标注
plt.xticks(range(n), word_list[0:n])
# 设置y轴刻度：最小为0，最大为cnt_list中的最大值+10，间隔10
plt.yticks(range(0, max(cnt_list) + 10, 10))

# 设置图片大小
# plt.figure(figsize = (20,20))
plt.savefig("短文人物词频统计图.png")
plt.show()
