"""
Date: 2021.2.9
Author: Justin

要点说明：
如何声明变量
变量的两大优势：便于多次使用，易于修改
"""

name1 = '刘备' # 给变量name1赋值
print(name1)   # 引用变量name1的值
# 注意：和其他编程语言不同，Python的变量不用声明类型

name2 = '关羽'   
name3 = '张飞' 

# 下面是多次引用变量
print('---------------------')
print(name1, name2, name3)  # 用print打印多个变量，用逗号分隔

name4 = name1  # 用已经赋值的变量name1给变量name4赋值
print('---------------------')
print(name1, name2, name3, name4)


