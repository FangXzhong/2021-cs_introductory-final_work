"""
Date: 2021.01.31
Author: Justin

要点说明：
1. 用input()要求用户输入
2. 用while结构检查输入，如果不符合条件，则要求重新输入，直到符合条件为止
3. 注意：这段代码中存在两行功能重复的代码，即输入input()和类型转换int()。需要优化
"""

total_players = input('请输入参加编程大赛的总人数：')
total_players = int(total_players)  # 转换成整数类型
# 再强调一下，目前都假定用户会按要求输入整数，不处理类型错误（比如输入字母）

while total_players < 0: # 检查参赛人数，不能为负数
    print('人数不能为负数！')
    total_players = input('请输入参加编程大赛的总人数：')
    total_players = int(total_players)  # 转换成整数类型    

print('-----完成-----')

