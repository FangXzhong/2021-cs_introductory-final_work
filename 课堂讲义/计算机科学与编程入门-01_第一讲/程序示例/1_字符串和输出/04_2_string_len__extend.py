"""
Date: 2021.2.9
Author: Justin

要点说明：
学习print之外的第2个函数：返回字符串长度的len函数
len函数和print函数不同在于：有返回值
"""

msg = 'abcdefghi'
print(msg)

msg_length = len(msg)
# 函数len(字符串)会返回字符串的长度，即包含的字符数，可以将返回值赋给变量
print(msg_length)

print(len(msg))  
# 如果后面不需要再用到字符串的长度，也可以在print函数的括号中直接写len(字符串)
# 这样少一次变量赋值，代码比较简洁

# 注意，如果字符串是多行的文字，返回的长度数值是包含换行符的
msg = '''abc
def
ghi'''
print(len(msg))