"""
Date: 2021.3.10
Author: Justin

要点说明：
1、素材为一段中文故事文本
2、用jieba库分词，用字典统计两字以上的词的出现次数
3、去掉不想统计的词（只统计人名）
4、合并指代同一个人的名字
5、相比前一个程序示例，新增之处用明显的注释块标出了
"""

import jieba

# 待分析的文本
content = '''刘皇叔带着关羽、张飞去隆中拜访诸葛亮。不巧，\
诸葛亮外出游玩，不知何时回来。过了一段时间，在一个大雪天，他们\
又去了隆中，还是没有见到。
    新年之后，他们第三次来到隆中。这次，诸葛亮正好在家午睡。刘备\
让关羽、张飞留在门外，自己站在台阶下静静等候。过了很久，书童说\
孔明先生醒了。刘备进屋拜见诸葛亮，向他请教天下大势。这就是“三顾\
茅庐”和“隆中对”的故事。'''

# =============================================================================
# 先运行一次词频统计，挑出要忽略不统计的词，放到下面列表中
# =============================================================================
ignore_list = ['卧龙岗', '隆中']  # 为了简便，只挑出了出现次数较多的词

# 分词
word_list = jieba.lcut(content)

# print(word_list)
# input('按回车键继续……')

# 用字典统计每个词的出现次数
word_dict = {}
for w in word_list:
    if (len(w)) == 1:  # 跳过单字
        continue

    # =============================================================================
    # 跳过在忽略词列表中的词
    # =============================================================================
    if w in ignore_list:
        continue

    # =============================================================================
    # 合并指代同一个人的名字    
    # =============================================================================
    if w == '刘皇叔':
        w = '刘备'
    elif w == '孔明':
        w = '诸葛亮'

    if w in word_dict.keys():  # 已在字典中的词，将出现次数增加1
        word_dict[w] = word_dict[w] + 1
    else:  # 未在字典中的词，表示是第一次出现，添加进字典，次数记为1
        word_dict[w] = 1

# 把字典转成列表，并按原先“键值对”中的“值”从大到小排序
items_list = list(word_dict.items())
items_list.sort(key=lambda x: x[1], reverse=True)

total_num = len(items_list)
print('经统计，共有' + str(total_num) + '个不同的词')

# =============================================================================
# 设定限制，出现次数达到2次以上才输出
# =============================================================================
cnt_limit = 2
print('出现{}次以上的词如下：'.format(cnt_limit))

# 将结果输出到屏幕上
for i in range(total_num):
    word, cnt = items_list[i]
    if cnt < cnt_limit:
        break
    print(str(i + 1) + '.' + word + '\t' + str(cnt))

print('-----完成-----')
