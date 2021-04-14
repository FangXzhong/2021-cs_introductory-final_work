"""
Date: 2021.01.31
Author: Justin

要点说明：
循环结构的巨大威力：可以只写一小段代码，让计算机快速的、反复执行很多次同样的工作
例如，将同一段字符串打印100遍。不需要写100次print(),只需要写1次
注意，这里用到了用于循环次数计数的变量，通常简称“循环变量”
"""

count = 0  # 初始化循环变量，一般从0开始

while count < 100:  # 检查循环变量
    print('欢迎参加编程大赛')  # 每次打印的内容都是一样的
    count = count + 1  # 更新循环变量。如果忘记这条语句，会导致“死循环”

print('-----完成-----')

## 附加说明1
# count = count + 1 也可以写成： count += 1
# “+=”是一个特殊的运算符，这里表示将count自身加1，不推荐新手使用，但要能看懂
# 示例： a += 5 和 a = a + 5 是同样的操作

## 附加说明2
# 注意while的判断条件的设置，尤其是想清楚用“<”还是“<=”
# 这里要确保执行了100次，而不是99次或101次


