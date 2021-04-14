"""
Date: 2020.10.13
Author: Justin

要点说明：
浮点数（float）的声明和运算
"""

x = 36    
y = 5    
z = x / y   # 整数除法的结果是浮点数
print(z)

# ------------------
x = 3.5
y = 1.3
z = x - y   # 浮点数运算的结果是浮点数
print(z)

# ------------------
x = 3.5
y = 1
z = x * y   # 整数和浮点数运算的结果是浮点数
print(z)

# ------------------
x = 5.0     # 5是整数，5.0是浮点数
y = 1
z = x + y   
print(z)


print('-'*20) # 分隔线
# ------------------
# 有时浮点数会出现运算结果不精确的现象
x = 10.2
y = 9
z = x - y
print(z) # 结果是1.2吗？

# 如果需要确保精确结果，还需要学习后续的方法。例如，使用Decimal库
# 初学者先多使用整数（int）进行练习
