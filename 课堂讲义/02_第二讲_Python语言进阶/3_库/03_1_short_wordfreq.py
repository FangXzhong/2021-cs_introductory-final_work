"""
Date: 2021.3.10
Author: Justin

要点说明：
1、素材为一段中文故事文本
2、用jieba库分词，用字典统计两字以上的词的出现次数
3、按出现次数从多到少排序，并打印结果
"""

import jieba

# 待分析的文本
content = '''刘备和关羽、张飞去隆中卧龙岗拜访诸葛亮。不巧，\
诸葛亮外出游玩，不知何时回来。过了一段时间，在一个大雪天，他们\
又去了隆中，还是没有见到诸葛亮。
    新年之后，刘、关、张三人第三次来到卧龙岗。这次，诸葛亮正好\
在家午睡。刘备让关羽、张飞留在门外，自己站在台阶下静静等候。\
过了很久，书童说孔明先生醒了。刘备进屋拜见诸葛亮，向他请教天下\
大势。这就是“三顾茅庐”和“隆中对”的故事。'''

# 分词
word_list = jieba.lcut(content)

print(word_list)
input('按回车键继续……')

# 用字典统计每个词的出现次数
word_dict = {}
for w in word_list:
    if (len(w)) == 1:  # 忽略单字
        continue

    if w in word_dict.keys():  # 已在字典中的词，将出现次数增加1
        word_dict[w] = word_dict[w] + 1
    else:  # 未在字典中的词，表示是第一次出现，添加进字典，次数记为1
        word_dict[w] = 1

# 把字典转成列表，并按原先“键值对”中的“值”从大到小排序
items_list = list(word_dict.items())
items_list.sort(key=lambda x: x[1], reverse=True)

total_num = len(items_list)
print('经统计，共有' + str(total_num) + '个不同的词')

# 将结果打印在屏幕上
for i in range(total_num):
    word, cnt = items_list[i]
    print(str(i + 1) + '.' + word + '\t' + str(cnt))

print('-----完成-----')
