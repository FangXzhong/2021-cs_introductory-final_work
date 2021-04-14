"""
Date: 2020.10.13
Author: Justin

要点：
1. 字符串和数字的混合打印
2. 用str()函数将数字转换成字符串
"""

a = 36
b = 5
c = a + b

print('a+b=', c) # 注意，用逗号分隔的参数，运行时显示会有空格分隔

# print('a+b='+c) # 之前学过，可以用加号连接多个字符串，但连接字符串和数字时会报错。试一试

print('a+b=' + str(c))  # 用str函数把数字转换成字符串，就可以用加号连接了

c = a - b
print('a-b=' + str(c))
c = a * b
print('a×b=' + str(c))
c = a / b
print('a÷b=' + str(c))
