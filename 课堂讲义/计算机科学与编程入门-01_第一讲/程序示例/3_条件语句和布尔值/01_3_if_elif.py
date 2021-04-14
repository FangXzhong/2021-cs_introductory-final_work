"""
Date: 2021.01.26
Author: Justin

要点说明：
程序的多分支结构，用if-elif-else结构
"""

print('欢迎来到Python编程的课堂')
name = input('请输入姓名：')

# 如果 “字符串name的内容等于'Tom'”这个判断是“真”的，那么：
#      做事情A
# 否则，如果“字符串name的内容等于'Jerry'”这个判断是“真”的，那么：
#      做事情B
# 否则：
#      做事情C

if name.lower() == 'tom':
    print(name + '，你好！请坐在第一排。')
elif name.lower() == 'jerry':
    print(name + '，你好！请坐在最后一排。')
else:
    print(name + '，你好！请随意就坐。')

print('课程即将开始，请保持安静。谢谢！')