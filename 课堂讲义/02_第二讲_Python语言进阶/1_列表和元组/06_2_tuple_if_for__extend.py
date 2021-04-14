"""
Date: 2020.11.03
Author: Justin

要点说明：
元组（tuple）与列表类似的if/for操作
"""

# 声明元组
name_tup = ('刘备', '关羽', '张飞')

# 遍历元组
for name in name_tup:
    print(name)

print('-'*20)

# 检查元组是否包含特定元素
name_chk = '赵云'
if name_chk in name_tup:
    print('找到：' + name_chk)
else:
    print('没有找到：' + name_chk)

