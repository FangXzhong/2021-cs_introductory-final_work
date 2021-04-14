"""
Date: 2020.10.13
Author: Justin

要点说明：
1、用int()将输入的字符串转换为整数进行运算
2、可以处理所有整数，正、负、零
3、如果输入小数，则会报错
4、如果输入字母等非数字的字符，则会报错
"""

print('---看我给你做一道加法题--')
a = input('请输入一个整数：')
a = int(a)

b = input('请再输入一个整数：')
b = int(b)

c = a + b

print('****************')
print('它们加起来是：' + str(c))
print('****************')

print('type(a):', type(a))
print('type(b):', type(b))
print('type(c):', type(c))