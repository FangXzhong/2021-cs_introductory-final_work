"""
Date: 2021.01.31
Author: Justin

要点说明：
循环变量除了计数，还可以在循环语句中使用，从而让循环的每一次运行有所不同
例如，编程大赛要为每位选手提前安排机位指示字条，单号选手到东区机房，双号选手到西区机房。
"""

player_num = 0  # 用选手序号作为循环变量，变量名更加明确指明了含义

while player_num < 100:  # 假设本次比赛最多100人参赛
    player_num = player_num + 1  # 先更新选手序号，让输出从1开始，更符合现实中的习惯
    if player_num % 2 == 0:
        print('第{}位选手：西区机房'.format(player_num))  # 双号选手
    else:
        print('第{}位选手：东区机房'.format(player_num))  # 单号选手

print('-----完成-----')

