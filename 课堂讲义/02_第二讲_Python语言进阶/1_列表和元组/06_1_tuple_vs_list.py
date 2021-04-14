"""
Date: 2021.3.7
Author: Justin

要点说明：
1、元组（tuple）与列表类似，不同之处在于元组的元素不能修改
2、元组使用小括号 ( )，列表使用方括号 [ ]
"""

# 声明元组
name_tup = ('刘备', '关羽', '刘备', '张飞', '关羽', '刘备')

print(type(name_tup))  # 查看元组类型

# 访问元组元素，和访问列表方式相同
print(name_tup[1])
print(name_tup[2:5])
print(name_tup[-1])

# 元组元素不可被修改，下面的操作会报错
name_tup[0] = '大耳贼'
