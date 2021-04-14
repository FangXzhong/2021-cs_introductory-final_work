"""
Date: 2021.3.7
Author: Justin

要点说明：
如何复制列表？
用等号赋值，如list2=list1，只是设置了“别名”（alias）
用list2 = list1[:]的形式才会真的复制产生一个新的列表
"""

name_list = ['刘备', '关羽', '刘备', '张飞', '关羽', '刘备' ]

print('-----复制列表-----')
name_list_bak2 = name_list[:] 
    
print('-----修改原列表-----')
name_list[-1] = '大耳贼'  # 改变name_list的一个元素
for name in name_list:
    print(name)  # name_list确实改变了，

print('-----检查新列表-----')
for name in name_list_bak2:
    print(name)  # name_list_bak2没有改变
# 这样证明name_list和name_list_bak2不是同一个列表
