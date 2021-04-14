"""
Date: 2020.12.01
Author: Justin

要点说明：
1、jieba.add_word()函数增加新词
2、jieba.del_word()函数删除指定词
3、jieba.load_userdict()函数添加自定义词典
"""

import jieba

# 如何识别不常见的词
txt = '易烊千玺有时被“粉丝”叫做四字弟弟。'
word_list = jieba.lcut(txt)  # 无法识别
print(word_list)

# 动态调整词库：add_word()，del_word()
jieba.add_word('易烊千玺')  # 添加指定词
word_list = jieba.lcut(txt)  # 现在可以识别
print(word_list)

jieba.del_word('易烊千玺')  # 删除指定词
word_list = jieba.lcut(txt)  # 现在无法识别
print(word_list)

print('-' * 20)
# 可以事先将自定义的词放在文本文件中，称为“自定义字典”
# 自定义字典的编码格式必须为“utf-8”。用文本编辑器另存时，选择“编码”
jieba.load_userdict('./data/userdict.txt')
word_list = jieba.lcut(txt)
print(word_list)

# 恢复原状
jieba.del_word('易烊千玺')  # 删除指定词
