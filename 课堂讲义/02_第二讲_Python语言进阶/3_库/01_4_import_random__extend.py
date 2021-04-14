"""
Date: 2021.3.10
Author: Justin

要点说明：
加载内置库，调用库中的方法
"""

import random  # 加载随机数库，可以生成随机数

for i in range(10):
    x = random.randint(0, 100)  # 随机生成0~100之间的整数，包含0和100
    print(x, end=' ')

print()
