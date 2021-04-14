"""
Date: 2021.3.10
Author: Justin

要点说明：
1、读入《三国演义》中文小说文本，用jieba库分词
2、用字典统计两字以上的词的出现次数
3、删除不是人名的词
4、对指代同一人物的人名进行合并
5、根据用户需求，打印出现次数最多的若干个人物名字和出现次数
6、上述打印结果同时写入结果文件
"""

import jieba

txt_filename = './data/三国演义.txt'
result_filename = './output/三国演义-人物词频.csv'

ignore_list = ['将军', '却说', '二人', '不可', '荆州', '不能', '如此',
               '商议', '如何', '主公', '军士', '左右', '军马', '次日',
               '引兵', '大喜', '天下', '东吴', '于是', '今日', '不敢',
               '魏兵', '陛下', '人马', '都督', '一人', '不知', '汉中',
               '众将', '只见', '蜀兵']

# 从文件读取文本
txt_file = open(txt_filename, 'r', encoding='utf-8')
content = txt_file.read()
txt_file.close()

# 分词
word_list = jieba.lcut(content)

# 用字典统计每个词的出现次数
word_dict = {}
for w in word_list:
    # 跳过单字
    if len(w) == 1:
        continue

    # 跳过不想统计的词
    if w in ignore_list:
        continue

    # 对指代同一人物的名词进行合并
    if w == '孔明':
        w = '诸葛亮'
    elif w == '玄德' or w == '刘玄德':
        w = '刘备'
    elif w == '云长' or w == '关公':
        w = '关羽'
    elif w == '后主':
        w = '刘禅'
    else:
        pass  # pass表示“什么都不做”，常用于为尚未完成的代码占位置

    # 已在字典中的词，将出现次数增加1；否则，添加进字典，次数记为1
    if w in word_dict.keys():
        word_dict[w] = word_dict[w] + 1
    else:
        word_dict[w] = 1

# 把字典转成列表，并按原先“键值对”中的“值”从大到小排序
items_list = list(word_dict.items())
items_list.sort(key=lambda x: x[1], reverse=True)

total_num = len(items_list)
print('经统计，共有' + str(total_num) + '个不同的词')

# 根据用户需求，打印排名前列的词，同时把统计结果存入文件
num = input('您想查看前多少个人物？[10]:')
if not num.isdigit() or num == '':  # 如果输入的不全是数字，或者直接按了回车
    num = 10  # 设成查看前10名
else:
    num = int(num)  # 如果输入了正常的数字，则按用户需求设置

result_file = open(result_filename, 'w')  # 新建结果文件

result_file.write('人物,出现次数\n')  # 写入标题行

for i in range(num):
    word, cnt = items_list[i]
    message = str(i + 1) + '. ' + word + '\t' + str(cnt)
    print(message)
    result_file.write(word + ',' + str(cnt) + '\n')

result_file.close()  # 关闭文件

print('已写入文件：' + result_filename)

# =============================================================================
# 分词的一些细节处理
# =============================================================================

# jieba分词会有一些疏漏。例如，“玄德曰”被当做一个词，没有切分开
# 首先想到的是把“玄德曰”合并到“刘备”里，“孔明曰”也可以同样处理
# 但是，进一步分析会发现，“操曰”没有被当做一个词
# 如果把“玄德曰”合并到“刘备”里，那“曹操”的统计就偏少了，缺少了“操曰”
# 可以用自定义字典方式添加：jieba.add_word('操曰')。再把“操曰”合并到“曹操”里 
# 但是，这样会进一步带来新的问题，比如“权曰”和“孙权”的关系
# 通过检查发现，操曰、玄德曰、孔明曰的数量差不多，为了简便，这些都不统计
# 因此，需要注意的是，词频统计和文本自身特点有很大关系，要具体问题具体分析
