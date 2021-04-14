"""
Date: 2021.01.26
Author: Justin

要点说明：
if-else是程序分支结构，表示：

如果 这个判断的结果是“真”，那么：
    做事情A（可以有多行代码）
否则：
    做事情B（可以有多行代码）
    
注意if-else结构中的冒号和缩进
"""

print('欢迎来到Python编程的课堂')
name = input('请输入姓名：')

# 如果 “字符串name的内容等于'Tom'”这个判断是“真”的：
#      做事情A
# 否则：
#      做事情B
if name.lower() == 'tom':  
    print('~'*20)
    print(name + '，你好！请坐在第一排。')
    print('~'*20)
else:
    print('-'*20)
    print(name + '，你好！请随意就坐。')
    print('-'*20)
    
print('课程即将开始，请保持安静。谢谢！')