"""
Date: 2021.3.9
Author: Justin

要点说明：
1、用if语句检查指定内容是否在字典中
2、keys()函数返回字典里所有的键
3、values()函数返回字典里所有的值
4、items()函数返回字典里所有的“键值对”
"""

name_dict = {'刘备': 3,
             '关羽': 2,
             '张飞': 1,
             '诸葛亮': 5,
             }

print(name_dict.keys())  # 返回字典中所有的键
print(name_dict.values())  # 返回字典中所有的值
# 注：上面函数返回的都是类似列表的形式，可以当做列表使用

print('---检查某个“键”---')
if '张飞' in name_dict.keys():
    print('找到！')

print('---检查某个“值”---')
if 5 in name_dict.values():
    print('找到！')

print('-' * 20)

# 返回字典中所有的“键值对”，注意“键值对”是元组的形式
print(name_dict.items())

print('---检查某个“键值对”---')
if ('关羽', 2) in name_dict.items():  # 这里元组的圆括号可以不加，效果相同
    print('找到！')
