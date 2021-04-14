# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 17:58:39 2020
@author: Justin
"""
'''
使用Faker函数库生成模拟数据
'''

from pyecharts.faker import Faker

x = Faker.choose()
print('choose():')
print(x)

x = Faker.clothes
print('clothes')
print(x)

x = Faker.months
print('months')
print(x)

x = Faker.provinces
print('provinces')
print(x)

x = Faker.values()
print('values()')
print(x)