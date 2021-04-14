"""
Date: 2021.3.7
Author: Justin

要点说明：
1、更新字典内容：修改、添加、删除、清空等
2、修改和添加用同样的方式，这也保证了列表的“键”不会重复
"""

name_dict = {'刘备': 3,
             '关羽': 2,
             '张飞': 1,
             '诸葛亮': 5,
             }

# 更新字典中的内容
name_dict['张飞'] = 4
print(name_dict['张飞'])

# 向字典添加内容，方式和更新字典内容一样，区别在于使用了新的“键”
name_dict['赵云'] = 3
print(name_dict['赵云'])

print('-' * 20)
print(name_dict)

print('-' * 20)
# 删除字典中的“键值对”。注意，删除不存在的“键”会导致程序报错
del name_dict['关羽']
print(name_dict)

print('-' * 20)
# 清空字典
name_dict.clear()
print(name_dict)
print('字典长度：' + str(len(name_dict)))
