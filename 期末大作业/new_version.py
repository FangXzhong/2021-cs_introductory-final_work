import threading
import requests
from queue import Queue
from threading import Thread
from pyquery import PyQuery as pq
import get_the_raw_information


class NewBeikeParse(Thread):
    """
    新版爬取贝壳二手房的爬虫对象
    """
    def __init__(self, url, city, q):
        super(NewBeikeParse, self).__init__()
        self.url = url
        self.city = city
        self.q = q  # 这是一个Queue()对象
        # self.headers = {}

    def run(self):
        with new_beike_sem:
            self.new_beike_parse()
            global new_beike_count
            new_beike_count += 1
            if new_beike_count % 100 == 0:
                print("已经处理{}条消息".format(new_beike_count))

    def new_beike_parse(self):
        data_dict = dict()
        data_dict['所属城市'] = self.city

        raw_html = requests.get(self.url).text
        pq_doc = pq(raw_html)
        page_house_list = list()
        content_list = pq_doc(
            '#__layout > div > section > section.list-main > section.list-left > section:nth-child(4)')

        for i in range(60):
            # 逐个找到信息
            data_dict['地址'] = pq_doc(
                '#__layout > div > section > section.list-main > section.list-left > section:nth-child(4) > '
                'div:nth-child({}) > a > div.property-content > div.property-content-detail > section > '
                'div.property-content-info.property-content-info-comm > p.property-content-info-comm-address > '
                'span:nth-child(1)'.format(str(i + 1))).text().strip() + pq_doc(
                '#__layout > div > section > section.list-main > section.list-left > section:nth-child(4) > div:nth-child({}) '
                '> a > div.property-content > div.property-content-detail > section > '
                'div.property-content-info.property-content-info-comm > '
                'p.property-content-info-comm-address > span:nth-child(2)'.format(str(i + 1))).text().strip() \
                              + pq_doc(
                '#__layout > div > section > section.list-main > section.list-left > section:nth-child(4) > div:nth-child({})'
                ' > a > div.property-content > div.property-content-detail > section > '
                'div.property-content-info.property-content-info-comm > p.property-content-info-comm-name'.format(
                    str(i + 1))).text().strip()
            # print(data_dict['地址'])

            # 这里取两个的最大值是因为，有的房源房主并没有报价，贝壳平台会给出一个参考价，所以取最大值，
            # 而由于数字的ASC码是递增的，所以直接比较字符串大小就行
            data_dict['总价'] = pq_doc('#__layout > div > section > section.list-main > section.list-left > '
                                     'section:nth-child(4) > div:nth-child({}) > a > div.property-content > '
                                     'div.property-price > p.property-price-total > '
                                     'span.property-price-total-num'.format(str(i + 1))).text()

            data_dict['单价'] = pq_doc(
                '#__layout > div > section > section.list-main > section.list-left > section:nth-child(4) > '
                'div:nth-child({}) > a > div.property-content > div.property-price > '
                'p.property-price-average'.format(str(i + 1))).text()
            data_dict['格局'] = pq_doc("#__layout > div > section > section.list-main > section.list-left > "
                                     "section:nth-child(4) > div:nth-child({}) > a > div.property-content > "
                                     "div.property-content-detail > section > div:nth-child(1) > "
                                     "p.property-content-info-text.property-content-info-attribute".format(str(i + 1))) \
                .text().replace('\n', "")
            data_dict['面积'] = pq_doc('#__layout > div > section > section.list-main > section.list-left > '
                                     'section:nth-child(4) > div:nth-child({}) > a > div.property-content > '
                                     'div.property-content-detail > section > div:nth-child(1) > p:nth-child(2)'
                                     .format(str(i + 1))).text()
            data_dict['建成时间'] = pq_doc('#__layout > div > section > section.list-main > section.list-left > '
                                       'section:nth-child(4) > div:nth-child({}) > a > div.property-content > '
                                       'div.property-content-detail > section > div:nth-child(1) > p:nth-child(5)'
                                       .format(str(i + 1))).text().split('年')[0].strip()
            data_dict['信息来源'] = '安居客'
            item = pq_doc('#__layout > div > section > section.list-main > section.list-left > section:nth-child(4) > '
                          'div:nth-child({})'.format(str(i + 1)))
            data_dict['原网址'] = pq(item)('a').attr('href')

            # print(list(data_dict.values()))
            page_house_list.append(list(data_dict.values()))  # 一个房源的信息
        return page_house_list


def new_beike(city="北京", proxy=None):
    """
    爬取贝壳二手房的二手房信息
    """
    if proxy is None:
        proxy = {}
    print('正在获取贝壳二手房{}的房源数据……'.format(city))
    if proxy:
        beike_house_list = get_the_raw_information.beike_get_url(city, proxy)  # 贝壳二手房房源url列表
    else:
        beike_house_list = get_the_raw_information.beike_get_url(city)  # 贝壳二手房房源url列表

    # 创建一个队列用于保存线程获取到的所有数据
    q = Queue()

    # 保存线程
    Thread_list = list()

    global new_beike_sem
    new_beike_sem = threading.Semaphore(10)
    global new_beike_count
    new_beike_count = 0
    for url in beike_house_list:
        p = NewBeikeParse(url, city, q)
        p.start()
        Thread_list.append(p)
