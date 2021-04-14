"""
Date: 2021.3.9
Author: Justin

要点说明：
1、复制字典不能直接用等号赋值，这样只是建立一个“别名”（alias）。这和复制列表类似
2、“别名”可以理解成对同一个字典起了个新名字，新老名字都在用
3、要达到复制的效果，可以先建立一个空字典，再用update()函数合并字典
"""

name_dict = {'刘备': 3,
             '关羽': 2,
             '张飞': 1,
             '诸葛亮': 5,
             }

new_name_dict = name_dict  # new_name_dict只是一个别名
new_name_dict['张飞'] = 4  # 改变new_name_dict，其实就是改变name_dict
print(new_name_dict)
print(name_dict)

print('-' * 20)

# 真正的复制字典
name_dict = {'刘备': 3,
             '关羽': 2,
             '张飞': 1,
             '诸葛亮': 5,
             }

new_name_dict = {}  # 建立一个空字典
new_name_dict.update(name_dict)  # 将name_dict的内容复制到new_name_dict，现在两个字典内容相同
new_name_dict['张飞'] = 4  # 改变new_name_dict，不会影响name_dict
print(new_name_dict)
print(name_dict)
