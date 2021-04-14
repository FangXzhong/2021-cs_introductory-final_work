"""
Date: 2021.3.10
Author: Justin

要点说明：
1、在之前示例的基础上更新了文件读写
2、待分析的文本从文件读入
3、统计结果写到文件中
"""

import jieba

# 待分析的文本和输出结果的文件名
txt_filename = './data/短文.txt'
result_filename = './output/短文-人物词频.csv'

# 从文件读取待分析的文本
txt_file = open(txt_filename, 'r', encoding='utf-8')
content = txt_file.read()
txt_file.close()

# 忽略词列表
ignore_list = ['卧龙岗', '隆中', '他们']

# 分词
word_list = jieba.lcut(content)

# print(word_list)
# input('按回车键继续……')

# 用字典统计每个词的出现次数
word_dict = {}
for w in word_list:
    if (len(w)) == 1:  # 跳过单字
        continue

    # 跳过在忽略词列表中的词
    if w in ignore_list:
        continue

    # 合并指代同一个人的名字    
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

# 设定限制，出现次数达到2次以上才输出
cnt_limit = 2
print('出现{}次以上的词如下：'.format(cnt_limit))

result_file = open(result_filename, 'w')  # 新建结果文件

result_file.write('人物,出现次数\n')  # 向结果文件中写入标题行

# 将统计情况输出到屏幕上，同时写入结果文件
for i in range(total_num):
    word, cnt = items_list[i]
    if cnt < cnt_limit:
        break
    print(str(i + 1) + '.' + word + '\t' + str(cnt))
    result_file.write(word + ',' + str(cnt) + '\n')

result_file.close()  # 关闭文件

print()
print('写入文件完成：' + result_filename)
