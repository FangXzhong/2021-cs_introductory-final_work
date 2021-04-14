"""
Date: 2021.2.9
Author: Justin

要点说明：
1、整数转换函数int()
2、类型检查函数type()
"""

# 将字符串转换为数字
x = '36'
y = '5'
# z = x - y  # 试一试，字符串不支持减法操作

a = int(x) # 用int函数把字符串a转换成整数
b = int(y)
c = a - b  # 转换成整数后，就可以正确运算了
print(c)

print('-'*20)  # 分隔线
# 查看变量的类型
print(type(x))
print(type(a))
print(type(c))

# 对非整数（如字母、小数或其它符号）用int函数，会报错
# x = int('A')
# x = int('3.14')
# x = int('@#$%')  


