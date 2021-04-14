"""
Date: 2020.10.13
Author: Justin

要点说明：
input()输入的都是字符串，如需输入整数，要另作处理
"""

print('---看我给你做一道加法题---')
a = input('请输入一个整数：')
b = input('请再输入一个整数：')
c = a + b

print()
print('****************')
print('它们加起来是：' + str(c))
print('****************')

print('type(a):', type(a))
print('type(b):', type(b))
print('type(c):', type(c))