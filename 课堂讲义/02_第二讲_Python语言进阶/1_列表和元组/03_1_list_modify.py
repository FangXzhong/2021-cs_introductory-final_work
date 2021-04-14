"""
Date: 2021.3.9
Author: Justin

要点说明：
修改、添加、删除列表中的元素
"""

name_list = ['刘备', '关羽', '刘备', '张飞', '关羽', '刘备' ]

for name in name_list:
    print(name)

print('-----修改单个元素-----')
name_list[2] = '刘玄德'
for name in name_list:
    print(name)

print('-----在最后添加一个元素-----')
name_list.append('赵云')
for name in name_list:
    print(name)

print('-----插入一个元素-----')
name_list.insert(2, '诸葛亮')
for name in name_list:
    print(name)
    
print('-----删除单个元素-----')
del name_list[3]
for name in name_list:
    print(name)

print('-----删除一段子列表-----')
del name_list[1:4]
for name in name_list:
    print(name)

print('-----清空列表-----')
name_list.clear()
for name in name_list:
    print(name)
    
print('列表元素数量：', len(name_list))






