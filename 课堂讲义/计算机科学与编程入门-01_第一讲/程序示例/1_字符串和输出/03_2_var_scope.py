"""
Date: 2021.2.9
Author: Justin

要点说明：
理解变量的作用域，也称作生命周期
因为程序语句是顺序执行的，所以对变量重新赋值后，只影响之后的代码
"""

msg = '你好' # 给变量msg赋值
print(msg)   # 引用变量msg的值

msg = 'hello'  # 再次给变量msg赋值
print(msg)   # 此时msg已经是新值





