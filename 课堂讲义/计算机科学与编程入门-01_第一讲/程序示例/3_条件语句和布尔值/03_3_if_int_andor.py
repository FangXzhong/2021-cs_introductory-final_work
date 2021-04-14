"""
Date: 2020.10.13
Author: Justin

要点说明：
1、在if的条件判断里，使用and/or逻辑操作符
2、if语句的嵌套使用
"""

# s = input('请输入你的成绩：')
# s = int(s)
s = 90  # 测试时可以直接给变量赋值，效率更高

if s >= 90 and s <= 100:  # and表示“且”，条件必须都满足
    print('成绩优秀')
    if (s == 100) or (s == 99) or (s == 98):  # or表示“或”，条件满足其一即可
        print('~~~看来这门课对你来说太简单了~~~')
elif s >= 70:
    print('成绩良好')
elif s >= 60:
    print('成绩合格')
elif s < 60 and s >= 0:
    print('不及格')
else:
    print('***输入不在0~100之间***')


