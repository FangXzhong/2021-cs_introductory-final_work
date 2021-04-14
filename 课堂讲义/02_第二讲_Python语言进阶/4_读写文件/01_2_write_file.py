"""
Date: 2021.3.10
Author: Justin

要点说明：
1、新建一个文本文件
2、将一些内容写入文件
3、生成的文件可以用文本编辑器打开
4、逗号分隔文件（CSV）也可以用Excel打开
"""

# 准备将下面的人名词频数据写到文件中
namefreq_list = [('刘备', 8),
                 ('诸葛亮', 6),
                 ('张飞', 3),
                 ('关羽', 2),
                 ]

result_filename = './output/test.csv'  # 待写入的目标文件名

result_file = open(result_filename, 'w', encoding='utf-8')  # 用“写”模式打开文件
# 如果指定utf-8编码，用Excel打开时可能会有显示问题，用文本编辑器打开没有问题
# 如果不指定编码格式，会根据当前系统设置选择一种编码，中文版Windows通常是ANSI格式（GBK格式）

result_file.write('词,次数\n')  # 写入标题行。如果要换行，要手动添加换行符（\n）

for i in range(len(namefreq_list)):
    word, cnt = namefreq_list[i]
    result_file.write(word + ',' + str(cnt) + '\n')
    # 遍历列表中每个元素，用逗号分隔、换行符结束的方式写入目标文件

result_file.close()  # 文件使用完毕，一定要关闭

print('已写入文件：' + result_filename)
# 分别用文本编辑器和Excel打开逗号分隔文件（CSV文件），查看效果
