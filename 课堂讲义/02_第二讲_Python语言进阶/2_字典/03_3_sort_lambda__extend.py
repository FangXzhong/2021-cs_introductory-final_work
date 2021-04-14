"""
Date: 2020.12.08
Author: Justin

要点说明：
列表由若干元组组成，按元组中某个元素的大小进行排序
"""

# list.sort(key=None, reverse=False)
# reverse=True 降序， reverse=False 升序（默认）

# 列表中的元素是元组，元组有2个元素
# 学生名，身高，体重
stu_list = [('Zhang', 170),
            ('Wang', 180),
            ('Li', 165),
            ('Zhao', 175),
            ('Liu', 170)]

# sort()无参数时，默认按每个元组的第0个元素排序
stu_list.sort()
for stu in stu_list:
    print(stu)

print('-' * 20)
# x[1]指定按每个元组的第1个元素排序，即按身高排序
stu_list.sort(key=lambda x: x[1])
for stu in stu_list:
    print(stu)

# ===========================================

# 列表中的元素是元组，元组有3个元素
# 学生名，身高，体重
stu_list = [('Zhang', 170, 70),
            ('Wang', 180, 70),
            ('Li', 165, 70),
            ('Zhao', 175, 90),
            ('Liu', 170, 80)]

# 先按体重排序，体重相等时再按身高排序
stu_list.sort(key=lambda x: (x[2], x[1]))

for stu in stu_list:
    print(stu)
