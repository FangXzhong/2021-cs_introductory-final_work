"""
Date: 2021.3.9
Author: Justin

要点说明：
1、用for循环遍历字典
2、keys()函数返回字典里所有的键
3、values()函数返回字典里所有的值
4、items()函数返回字典里所有的“键值对”
"""

name_dict = {'刘备': 3,
             '关羽': 2,
             '张飞': 1,
             '诸葛亮': 5,
             }

print('---打印“键”---')
print(name_dict.keys())
for key in name_dict.keys():
    print(key)

print('---打印“值”---')
print(name_dict.values())
for value in name_dict.values():
    print(value)

print('---打印“键值对”---')
print(name_dict.items())  # items()函数返回的是元组的列表
# for (key,value) in name_dict.items(): 这里可以加圆括号，也可以不加
for key, value in name_dict.items():
    print(key + '出现了' + str(value) + '次。')
