"""
Date: 2020.10.20
Author: Justin

要点说明：
一个简单的小例子，展示在while循环中使用break和continue的区别
"""

# 打印 1 2 3
i = 0
while i < 6:
    i = i + 1
    if i == 4:
        break  # break用于跳出循环，循环结束。
    print(i, end=' ')  
    # print打印时默认换行结束，但可以用end参数指定其它结束符号，这里指定了空格符

print()

# 打印 1 2 3 5 6 （没有4）
i = 0
while i < 6:
    i = i + 1
    if i == 4:
        continue  # continue表示跳过循环中本轮执行的后续语句，回到while的条件判断
    print(i, end=' ')

print()
print('演示结束')
