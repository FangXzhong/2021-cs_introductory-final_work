"""
    Date:2021.03.16
    Author:Fang Xiangzhong

    要点说明：
    1.本程序实现了对txt文件进行分词、词频统计排序的功能，最终的结果会以（词，词频）的格式保存
      在一个CSV文件中
    2.本程序的核心是TextAnalysis类，通过TextAnalysis的content属性读入待分析的文本文件，
      之后分别使用cut_into_words和count_the_times方法进行分词和计数，
      最后将结果通过save_the_result方法进行输出
    3.本程序依赖的库有jieba
"""
import jieba


class TextAnalysis:
    def __init__(self, text_filename, encoding_mode='utf-8'):
        """
        :param text_filename: 存储待分析的文本文件的文件名
        :param encoding_mode: 对文件的解码方式，默认为utf-8
        """
        self.content = open('./data/' + text_filename, "r", encoding=encoding_mode).read()
        # 用来保存待分析的文本
        self.word_list = list()  # 用来保存分词之后的文本
        self.sorted_list = list()  # 用来保存按照词频进行排序之后的文本
        self.total_num = 0  # 用来保存总共的词数量

        self.output_file = './output/{}_词频统计结果.csv'.format(text_filename.split('.')[0])
        #  结果文件输出路径

    def cut_into_words(self, user_dict=None):
        """
        此方法用于分词，可选输入参数是用户字典，用于用户自定义词汇。
        默认值为None而不是空字典是为了防止因为空字典是可变对象而可能带来的一些问题
        结果会保存在TextAnalysis.word_list属性中
        """
        if user_dict is None:
            user_dict = dict()
        if not user_dict == {}:
            jieba.load_userdict('./data/' + user_dict)
        self.word_list = jieba.lcut(self.content)

    def count_the_times(self, ignore_list=None, replace_dict=None):
        """
        这个方法用来对词频进行统计，其中可选的输入参数有ignore_list和replace_list，
        前者是让用户自定义不用统计的词，后者是针对某些意义为相同的词进行词频合计的（比如，
        本文中‘孙少平’和‘少平’就应该进行合并）
        方法的输出会保存在sorted_list和total_num两个属性内
        """
        if replace_dict is None:
            replace_dict = {}
        if ignore_list is None:
            ignore_list = []
        word_dict = {}  # 一个用来存储 词：词频 键值对的临时变量

        # 以下是防止用户在调用cut_into_words分词前就进行count_the_times操作而导致的错误输出
        if not self.word_list:
            flag = input('文本还没有分词，是否现在进行分词？y/n')
            if flag == 'y':
                self.cut_into_words()
            else:
                print('程序即将退出')
                exit()

        for word in self.word_list:
            if len(word) == 1 or word in ignore_list:  # 忽略词长度为1的以及用户自定义忽略的词
                continue
            if word in replace_dict.keys():  # 替换
                word = replace_dict[word]
            if word in word_dict.keys():
                word_dict[word] = word_dict[word] + 1
            else:
                word_dict[word] = 1
        self.sorted_list = sorted(list(word_dict.items()), key=lambda x: x[1],
                                  reverse=True)
        self.total_num = len(self.sorted_list)
        print('经统计，共有{}个不同的词'.format(self.total_num))

    def show(self, num=10):
        """
        :param num: 要保存的词的条目数，默认为1
        """
        for i in range(num):
            print(self.sorted_list[i])
        print('-' * 20)

    def save_the_result(self, num=10):
        """
        :param num: 要保存的词的条目数，默认为1
        """
        result_file = open(self.output_file, 'w', encoding='utf-8')
        result_file.write('人物,出现次数\n')
        for i in range(num):
            word, cnt = self.sorted_list[i]
            message = '{}.\t{}\t{}'.format(str(i + 1), word, str(cnt))
            print(message)
            result_file.write('{},{}\n'.format(word, str(cnt)))
        result_file.close()
        print('已写入文件：' + self.output_file)


if __name__ == '__main__':
    a = TextAnalysis(r'平凡的世界.txt', encoding_mode='ANSI')
    user_ignore_list = open('data/ignore_list.txt', encoding='utf-8').read()
    user_replace_dict = {item.split('，')[0].strip(): item.split('，')[1].strip()
                         for item in
                         open('./data/replace_dict.txt', encoding='utf-8').readlines()}

    a.cut_into_words()
    a.count_the_times(user_ignore_list, user_replace_dict)

    number = input('请输入您想查看的数量(推荐46及以下)：')
    if not number.isdigit() or number == '':  # 检查用户输入是否合法
        a.show()
        a.save_the_result()
    elif int(number) > a.total_num:
        # 如果用户请求的查看数量超过总共的词条数，就显示默认词条数
        print('很抱歉，您要查看的数量超过总数{}，将为您呈现10条内容'.format(a.total_num))
        a.show()
        a.save_the_result()
    else:
        a.show(int(number))
        a.save_the_result(int(number))
