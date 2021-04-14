"""
Date: 2020.10.27
Author: Justin

要点说明：
break是跳出整个循环
continue是结束循环的这一轮，进入循环的下一轮
"""

for i in range(10):
    if i == 5:
        break
    print(i, end=' ')  # 打印但不换行的方法

print()    

for i in range(10):
    if i == 5:
        continue
    print(i, end=' ')
