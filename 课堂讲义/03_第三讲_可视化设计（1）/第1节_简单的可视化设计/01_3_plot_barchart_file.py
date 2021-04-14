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

plt.bar(word_list, cnt_list)

plt.savefig("短文人物词频统计图.png")
plt.show()
