"""
Date: 2021.01.31
Author: Justin

要点说明：
1、if结构的“翻译”：
   if 判断条件:
       程序语句
       
   如果判断条件成立，那么 执行一次 if结构所属的程序语句
   要点：最多执行一次
   
2、while结构的“翻译”：
   while 判断条件:
       程序语句
   
   如果判断条件成立，那么 执行一次 while结构所属的程序语句
   然后再判断一次条件，如果条件成立，那么 再执行一次 while结构所属的程序语句
   然后再判断一次条件，……（重复该步骤，直到某一次判断条件不成立）
   
   注意：每做完一次，都回到while语句，检查条件是否还成立
"""

# if语句
coins = 10

print('最初游戏币数量：' + str(coins))
if coins > 0:
    coins = coins - 1
    print('投币1个。目前剩余游戏币数量：' + str(coins))

print('最终游戏币数量：' + str(coins))


print('-'*20)
# while语句，与上面代码的区别仅是将if替换成while
coins = 10

print('最初游戏币数量：' + str(coins))
while coins > 0:
    coins = coins - 1
    print('投币1个。目前剩余游戏币数量：' + str(coins))

print('最终游戏币数量：' + str(coins))