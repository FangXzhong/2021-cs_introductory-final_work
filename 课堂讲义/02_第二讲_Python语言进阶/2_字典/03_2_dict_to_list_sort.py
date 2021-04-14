"""
Date: 2021.3.9
Author: Justin

要点说明：
1. 基于列表中的人名，统计不同人名出现的次数，存放到字典中
2. 需要将统计结果按出现次数从多到少输出
3. 因为无法直接将字典按“值”排序，需要将字典转换成列表，然后排序
4. 这里排序会用到匿名函数lambda，该函数有很多变化，记住这里的用法即可
"""

name_list = ['刘备', '关羽', '刘备', '张飞', '关羽', '刘备',
             '曹操', '曹操', '诸葛亮', '曹操', '曹操', '诸葛亮',
             '曹操', '诸葛亮', '刘备', '诸葛亮', '曹操', '诸葛亮']

name_dict = {}  # 生成空字典

# 遍历列表，生成字典
for name in name_list:  # 遍历列表中的人名
    if name in name_dict.keys():  # 如果当前人名在字典中，则出现次数加1
        name_dict[name] = name_dict[name] + 1
    else:  # 如果当前人名不在字典中，说明该人名第一次出现，出现次数初始值设为1
        name_dict[name] = 1

# 打印字典，检查结果
for key, value in name_dict.items():
    print(key + ': ' + str(value))

input('press enter ...')  # 暂停，以便查看打印结果

# 将字典的“键值对”转换成列表
freq_list = list(name_dict.items())
print(freq_list)  # 可以看出：列表中的元素都是元组

input('press enter ...')  # 暂停，以便查看打印结果

# 需要将列表按元组中的第1个元素排序，即按原字典中的“值”排序
print(sorted(freq_list))  # 直接排序，不能达到效果
input('press enter ...')  # 暂停，以便查看打印结果

freq_list.sort(key=lambda x: x[1], reverse=True)
# sort函数的key参数指定排序的依据，该列表中的元素类型为元组，元组中包含2个元素
# 此处的x:x[1]表示，对于列表中的每个元素x，按照其中x[1]来排序。  
# 也就是将列表按元组中的第1个元素排序，即按原字典中的“值”排序
# 另一个参数reverse=True，表示降序排列

print(freq_list)

input('press enter ...')  # 暂停，以便查看打印结果

# 输出结果，这里已经是按人名出现次数从多到少排序
for (name, cnt) in freq_list:  # 遍历列表中每个元素（都是元组）
    print(name + ': ' + str(cnt))

# 现在，只需要有办法将文学作品中的所有人名依次摘出来，保存到列表中
# 就可以用上面的代码，统计出人名出现的次数，并按次数多少排序输出
