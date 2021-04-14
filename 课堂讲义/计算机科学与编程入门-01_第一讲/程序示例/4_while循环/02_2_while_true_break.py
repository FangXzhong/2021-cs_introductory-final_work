"""
Date: 2021.01.31
Author: Justin

要点说明：
1. 在前一个程序示例的基础上优化，消除了重复的代码
2. 用while True，确定至少进入循环内部一次
3. 配合循环内部的break语句，在符合某种条件时跳出循环
4. 注意：如果没有break语句，while True会导致“死循环”
"""

while True: # 判断条件为“真”，即永远成立。看似“死循环”，实则要用循环内部的break语句跳出
    total_players = input('请输入参加编程大赛的总人数：')
    total_players = int(total_players)  # 转换成整数类型
    if total_players >= 0: # 检查输入是否符合条件（即大于等于0）
        break  # 跳出循环，即：循环结束，去执行整个while循环结构之后的语句
    else: # 如果执行了这句else，循环是没有结束，接下去会回到while的条件判断
        print('人数不能为负数！')   

print('-----完成-----')

