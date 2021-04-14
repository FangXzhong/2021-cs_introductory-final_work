"""
Date: 2021.3.9
Author: Justin

要点说明：
1、字典由“键-值对”（key-value）组成
2、形式和日常的“英汉字典”形式类似
3、掌握根据“键”查找字典中对应的“值”
"""

# 声明一个字典，保存一段三国故事里人物出现的次数
name_dict = {'刘备': 3,  # 字符串'刘备'为键（key），整数3为值（value）
             '关羽': 2,
             '张飞': 1,
             '诸葛亮': 5,
             }
# 注：
# 1、字符串、数字都可以作为字典的“键”
# 2、字符串、数字、列表、字典都可以作为字典的“值”

print(name_dict)
print('字典长度：' + str(len(name_dict)))

print(name_dict['关羽'])  # “查字典”的方式为：字典名[键]

print(name_dict['曹操'])  # 字典名[不存在的键] 会导致程序出错
# 不确定的情况下，应该用if语句先检查键是否在字典中（后续讲解）
