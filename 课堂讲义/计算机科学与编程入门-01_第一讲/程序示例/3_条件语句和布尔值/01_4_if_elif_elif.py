"""
Date: 2021.01.26
Author: Justin

要点说明：
1、可以有多个elif
2、else最多只有一个（可以没有），而且必须放在最后
"""

print('欢迎来到Python编程的课堂')
name = input('请输入姓名：')

if name.lower() == 'tom':
    print(name + '，你好！请坐在第一排。')
elif name.lower() == 'jerry':
    print(name + '，你好！请坐在最后一排。')
elif name.lower() == 'spike':
    print(name + '，你好！请坐在窗户边。')
else:
    print(name + '，你好！请随意就坐。')

print('课程即将开始，请保持安静。谢谢！')