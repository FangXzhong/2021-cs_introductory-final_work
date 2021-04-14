"""
Date: 2021.3.9
Author: Justin

要点说明：
1、声明一个列表的常用方法
2、将列表作为一个整体输出
3、判断某个元素是否在列表中
"""

# 列表用方括号[]标记，列表中的元素用逗号分隔
# 列表中的元素可以是字符串、数字、变量
# 列表中的元素可以重复
name_list = ['刘备', '关羽', '刘备', '张飞', '关羽', '刘备']

digits_list = [3, 6, 5, 8, 1, 4, 7, 9, 0, 2]

name1 = '曹操'
num1 = 208
mix_list = ['赤壁', name1, num1, 220]

# 将列表作为一个整体输出，带有方括号和逗号
print(name_list)

# len()函数返回列表中的元素个数
print('列表元素数量：', len(name_list))

print('--------------------')
name = '吕布'
if name in name_list:  # 如果变量name的值在列表name_list中，那么……
    print(name + '在列表中')
else:
    print(name + '不在列表中')
