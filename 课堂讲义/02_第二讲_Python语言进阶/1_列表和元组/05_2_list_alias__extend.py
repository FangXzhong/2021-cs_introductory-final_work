"""
Date: 2021.3.7
Author: Justin

要点说明：
如何复制列表？
用等号赋值，如list2=list1，只是设置了“别名”（alias）
“别名”可以理解成对同一个列表起了个新名字
新老名字都指代同一个列表，并没有产生新的列表
"""

name_list = ['刘备', '关羽', '刘备', '张飞', '关羽', '刘备' ]

print('-----“复制”列表-----')
name_list_bak = name_list  
for name in name_list_bak:
    print(name)

print('-----修改原列表-----')
name_list[0] = '刘皇叔' # 修改name_list
for name in name_list:
    print(name)
    
print('-----检查新列表-----')
for name in name_list_bak:
    print(name)  # 打印后会发现，name_list_bak也变了

# 这样证明：name_list和name_list_bak是同一个列表
