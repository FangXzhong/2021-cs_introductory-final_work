"""
Date: 2021.3.10
Author: Justin

要点说明：
直接加载库中的方法
"""

from time import sleep  
# 解读：从“time库”中加载“sleep”方法
# 用这样加载方式，后续直接用sleep(n)即可，不用写time.sleep(n)
# 优点：代码比较简洁。缺点：看不出所属的库，有时影响理解代码

print('真相')
sleep(1)
print('只有')
sleep(2)
print('一个')