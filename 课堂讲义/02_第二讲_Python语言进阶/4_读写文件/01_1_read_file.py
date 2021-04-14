"""
Date: 2021.3.10
Author: Justin

要点说明：
1、打开一个文本文件
2、读出文件的全部内容，并打印到屏幕上
3、要注意文本文件有多种编码格式
"""

# 事先准备好文件，文件默认放在程序运行的目录下，否则要写明路径
# 一个点（.）表示当前目录，两个点（..）表示上一层目录
txt_filename = './data/短文.txt'

# 从文件读取文本
txt_file = open(txt_filename, 'r', encoding='utf-8')  # 打开文件 
# 三个参数分别为：文件名，打开方式（r表示只读，w表示写），文件的编码格式
# 如果不指定编码格式，则会采用系统默认设置，可能会和要打开的文件格式不一致，导致出错
# Python3的源代码采用uft-8格式

content = txt_file.read()  # 读入文件的全部内容

txt_file.close()  # 关闭文件。注意一定要关闭文件

print(content)

# =============================================================================
# 注：
# 当文件比较小时（例如几个kB或几个MB），用read()读取整个文件比较方便
# 当文件特别大时（例如几个GB，会导致占满内存），可以用read(n)指定读入前n个字符
# =============================================================================
