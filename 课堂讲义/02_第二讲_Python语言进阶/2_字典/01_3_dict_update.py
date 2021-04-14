"""
Date: 2021.3.9
Author: Justin

要点说明：
合并两个字典
"""

name_dict = {'刘备': 3,
             '关羽': 2,
             '张飞': 1,
             '诸葛亮': 5,
             }

HAN_dict = {'汉献帝': 2,
            '大将军': 4,
            '关羽': 5,
            }

HAN_dict.update(name_dict)  # 合并字典，将name_dict加入HAN_dict
print(HAN_dict)  # HAN_dict发生变化，注意重复键'关羽'的变化
print(name_dict)  # liu_dict字典仍然存在，保持不变
