# -*- coding: utf-8 -*-
"""
Created on Tue Mar  9 09:43:36 2021

@author: DEER
"""

# coding: utf-8
import matplotlib.pyplot as plt

# 可以理解为：导入matplotlib这个大工具包的pyplot小工具包，并且给它起一个别名，以便后续使用方便，不必每次写全称

# 准备数据
xdata = ['a', 'b', 'c', 'd']
ydata = [90, 70, 50, 30]

# 绘制柱状图
plt.bar(xdata, ydata)

# 保存图表
plt.savefig('test')
# 显示图表
plt.show()
