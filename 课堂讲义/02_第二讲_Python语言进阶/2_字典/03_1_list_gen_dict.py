"""
Date: 2021.3.9
Author: Justin

要点说明：
基于列表中的人名，统计不同人名出现的次数，存放到字典中
"""

name_list = ['刘备', '关羽', '刘备', 
             '张飞', '关羽', '刘备' ]

name_dict = {}  # 生成空字典

for name in name_list:  # 遍历列表中的人名
    if name in name_dict.keys(): # 如果当前人名在字典中，则出现次数加1 
        name_dict[name] = name_dict[name] + 1
    else: # 如果当前人名不在字典中，说明该人名第一次出现，出现次数初始值设为1 
        name_dict[name] = 1
    
    print(name_dict)  # 循环每一轮结束时，展示当前字典情况
    input('press enter ...')  # 暂停，以便查看

# print(name_dict)

for key,value in name_dict.items():
    print(key + ': ' + str(value))