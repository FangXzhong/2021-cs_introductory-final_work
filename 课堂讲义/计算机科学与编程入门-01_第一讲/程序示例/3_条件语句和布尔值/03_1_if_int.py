"""
Date: 2021.01.26
Author: Justin

要点说明：
1、在if的条件判断里，使用整数的比较
2、完善条件判断，提前处理超过100和负数
"""

# s = input('请输入你的成绩：')
# s = int(s)
s = 150  # 测试时可以直接给变量赋值，效率更高

if s > 100 or s < 0:
    print('***输入不在0~100之间***')   
elif s >= 90:
    print('成绩优秀')
elif s >= 70:
    print('成绩良好')
elif s >= 60:
    print('成绩合格')
elif s < 60:
    print('不及格')
else:
    print('出现未知情况')  # 这个分支不会被执行，但把else写全，以防考虑不周，是个好习惯



