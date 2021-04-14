"""
Date: 2021.3.7
Author: Justin

要点说明：
不按序号，而是按内容删除指定的元素
"""

name_list = ['刘备', '关羽', '刘备', '张飞', '关羽', '刘备']

for name in name_list:
    print(name)

print('------------------')
name_list.remove('关羽')  # 将列表中出现的第一个指定元素删除
for name in name_list:
    print(name)

print('------------------')
# 如果指定的元素内容不存在，remove()函数会报错退出
# 为避免出错，最好用if语句先判断元素是否在列表中
name = '周瑜'
if name in name_list:
    name_list.remove(name)
else:
    print('没有找到：' + name)
