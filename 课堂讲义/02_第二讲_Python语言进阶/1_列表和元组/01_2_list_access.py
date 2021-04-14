"""
Date: 2021.3.10
Author: Justin

要点说明：
1. 用“列表名[n]”的方式引用列表中的一个指定元素
2. 用“列表名[n:m]”引用列表中的一个范围（子列表）
"""

name_list = ['刘备', '关羽', '刘备', '张飞', '关羽', '刘备']

print('-----单个元素，编号从头开始-----')
print(name_list[0])  # 列表的元素编号从0开始
print(name_list[1])
print(name_list[2])

print('-----单个元素，编号从末尾开始-----')
print(name_list[-1])  # 列表的倒数第1个元素
print(name_list[-2])  # 列表的倒数第2个元素

print('-----子列表-----')
print(name_list[1:3])  # 注意，[1:3]表示从第1个到第3个之前（不包括第3个）
print(name_list[2:-1])  # 从第2个到倒数第1个（-1）之前（即倒数第2个）
print(name_list[2:])  # 从第2个到末尾（即倒数第1个）
print(name_list[:3])  # 从开头（即第0个）到第3个之前（即第2个）
print(name_list[0::2])  # 从第0个（即开头）到末尾，跨度为2（即隔一个选一个）
