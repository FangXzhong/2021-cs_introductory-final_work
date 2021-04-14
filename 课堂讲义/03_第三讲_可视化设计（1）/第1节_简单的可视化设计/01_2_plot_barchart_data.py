# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt

# 指定所用中文的字体
import os

"""
Created on Thu Feb 27 21:58:48 2020
@author: Justin 
modified by Deer Mar 17 2021
"""
'''
用matplotlib.pyplot库，画基本的折线图和柱状图
'''
# import matplotlib


if os.name == "nt":  # Windows系统
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 设置字体
else:  # MacOS系统
    plt.rcParams["font.family"] = 'Arial Unicode MS'
plt.rcParams['axes.unicode_minus'] = False  # 支持负号的正常显示

# 准备数据
word_list = ['诸葛亮', '刘备', '关羽', '张飞']
cnt_list = [90, 70, 50, 30]

# 绘制柱状图
plt.bar(word_list, cnt_list)

# 绘制图表标题、坐标轴标签
plt.title('人物词频统计')  # 图表标题
plt.xlabel('人物')  # x轴标签
plt.ylabel('出现次数')  # y轴标签
# 保存图表
plt.savefig('人物词频统计')
# 把图表绘制到屏幕上
plt.show()
