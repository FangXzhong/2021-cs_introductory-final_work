"""
Date: 2021.3.10
Author: Justin

要点说明：
用for循环可以实现指定次数的循环操作，比while更简便
"""

# 用for配合列表，实现指定次数的循环操作
for i in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
    print(i, end=' ')

print()

# 用for和range()函数实现指定次数的循环操作，更为简便
# 函数range(10)代表0~9共10个整数的序列，类似列表。试试传给range()不同的值
for i in range(1000):
    print(i, end=' ')

print()

# while和计数变量实现指定次数的循环操作，代码明显比for循环复杂
i = 0
while i < 10:
    print(i, end=' ')
    i = i + 1
