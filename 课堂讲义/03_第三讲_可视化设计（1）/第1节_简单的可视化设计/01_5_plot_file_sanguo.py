# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import os

"""
Created on Mon Mar 27 13:59:26 2021
@author: Deer
"""
'''
从文件读出数据后，绘制图表
'''

if os.name == "nt":  # Windows系统
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 设置字体
else:  # MacOS系统
    plt.rcParams["font.family"] = 'Arial Unicode MS'
plt.rcParams['axes.unicode_minus'] = False  # 支持负号的正常显示

src_filename = './三国演义-人物词频.csv'

src_file = open(src_filename, 'r')
line_list = src_file.readlines()
src_file.close()

word_list = []
cnt_list = []

# print(line_list)
del line_list[0]  # 删除csv文件中的标题行

for line in line_list:
    line = line.replace('\n', '')
    word_cnt = line.split(',')
    word_list.append(word_cnt[0])
    cnt_list.append(int(word_cnt[1]))

# print(word_list)
# print(cnt_list)

# n = len(cnt_list)
n = 10

plt.bar(range(n), cnt_list[0:n])
plt.xticks(range(n), word_list[0:n])
plt.yticks(range(0, max(cnt_list) + 100, 100))
plt.savefig("三国演义-人物词频.png")
plt.show()
