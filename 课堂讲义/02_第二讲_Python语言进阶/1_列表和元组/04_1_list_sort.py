"""
Date: 2021.3.9
Author: Justin

要点说明：
对列表的元素进行排序，有两种方法：
（1）不改变原有列表的：sorted(list)
（2）改变原有列表的：list.sort()

学习大多数编程语言时，都要学习如何实现排序，代码比较复杂
Python自带排序功能，非常简便
"""

digits = [3, 6, 5, 8, 1, 4, 7, 9, 0, 2]

# 依次打印列表digits中的元素
print('digits:\t\t', digits)

# sorted(digits)返回一个新的列表，其内容是digits的元素按从小到大排序
# sorted(digits)不改变digits的元素顺序
sorted_digits = sorted(digits)
print('sorted():\t', sorted_digits)

# 可以看到digits的元素顺序没有变化
print('digits:\t\t', digits)

# digits.sort()是将digits的元素按从小到大排序
# digits的内容会被改变
digits.sort()
print('.sort():\t\t', digits)

# digits.reverse()是将digits的元素反转顺序
# digits的内容会被改变
digits.reverse()
print('.reverse():\t', digits)
