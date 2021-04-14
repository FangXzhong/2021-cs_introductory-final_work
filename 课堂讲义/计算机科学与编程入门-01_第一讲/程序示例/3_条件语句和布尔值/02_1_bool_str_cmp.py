"""
Date: 2021.01.26
Author: Justin

要点说明：
字符串的各种逻辑判断：
等于（相等），不等于（不相等）
大于，小于，大于或等于，小于或等于
"""

name_1 = 'Tom'
name_2 = 'Jerry'

# 注意，一个等号“=”表示“赋值”，两个等号“==”表示“判断是否相等”
print(name_1 == 'Tom')  
print(name_1 == 'Jerry')
print(type(name_1 == 'Tom'))  # 检查逻辑判断结果的类型

print('-'*20)

print(name_1 == name_2)  # 判断两个变量是否“相等”
print(name_1 != name_2)  # 判断两个变量是否“不相等”

print('-'*20)

print(name_1 > name_2)  # 字符串比较的“大于”和“小于”是基于字母顺序
print('A' < 'Z')   # 字母顺序靠后的，编码数值大
print('Z' < 'a')   # 小写字母的编码数值，整体比大写字母的大
print('X' >= 'X')  # 大于或等于，满足其一即可
print('A' <= 'C')  # 小于或等于，满足其一即可

