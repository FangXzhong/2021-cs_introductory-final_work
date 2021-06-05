"""
    首先，我们需要爬取贝壳找房、房多多和安居客网站上的房源信息，每一条房源信息的格式为
    [所属城市,地址,总价,单价,格局,面积,建成时间,信息来源,原网址]

    此文件为主要的数据获取的方法集合，可以直接作为包进行导入。同时，只需要调用Beike(),Anjvke(),
    Lianjia()三个函数就能够分别获得指定城市在贝壳二手房、安居客、链家三个二手房平台上的二手房房源

    其中，链家和贝壳二手房使用了多线程，安居客由于其反爬机制，不得不使用代理，而由于代理的带宽限制，
    所以安居客只是单线程
    另一方面，由于安居客网站简介信息已经足够，因此不需要像其它两个网站那样去访问每一个房源网址，而
    只需要访问到整个房源列表页面就行，所以速度并没有落后太多

    注意：文件最终会存入https://8.136.117.159 linux服务器中的MySQL数据库中，
    数据库访问所需要的信息请参见 add_coodinate_information.py line 36
"""
import time
import threading
import pypinyin
import requests
from queue import Queue
from pyquery import PyQuery as pq
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from threading import Thread

import add_coodinate_information


class BeikeSpider(Thread):
    """
    爬取贝壳二手房的爬虫对象
    """

    def __init__(self, url, city, q, proxy=None):
        super(BeikeSpider, self).__init__()
        if proxy is None:
            proxy = {}
        self.url = url  # 房源信息的url
        self.city = city
        self.q = q  # 这是一个Queue()对象
        self.proxies = proxy  # 可选代理

    def run(self):
        """
        该方法继承于Thread类，本程序通过此方法实现线程的数量控制
        :return:
        """
        global beike_sem
        with beike_sem:  # 最大活跃线程数量,是一个threading.Semaphore(int)对象
            self.beike_parse_page()
            global beike_count   # 统计已经完成的房源数量
            beike_count += 1
            if beike_count % 100 == 0:
                print("已经处理{}条消息".format(beike_count))

    def beike_parse_page(self):
        """
        此方法用来从网站上找到特定的房源信息
        """
        data_dict = dict()
        data_dict['所属城市'] = self.city

        # 获取页面源代码，分有代理和无代理的情形
        if self.proxies:
            raw_html = requests.get(self.url, proxies=self.proxies).text
        else:
            raw_html = requests.get(self.url).text

        # 得到pyquery对象
        pq_doc = pq(raw_html)

        # 逐个找到信息
        data_dict['地址'] = pq_doc(
            '#beike > div.sellDetailPage > div:nth-child(6) > div.overview > div.content > div.aroundInfo > div.areaName '
            '> span.info > a:nth-child(1)').text().strip() + pq_doc('#beike > div.sellDetailPage > div:nth-child(6) > '
                                                                    'div.overview > div.content > div.aroundInfo > '
                                                                    'div.areaName > '
                                                                    'span.info > a:nth-child(2)').text().strip() + pq_doc(
            '#beike > div.sellDetailPage > div:nth-child(6) > div.overview > div.content > div.aroundInfo > '
            'div.communityName > a.info.no_resblock_a').text().strip()

        # 这里取两个的最大值是因为，有的房源房主并没有报价，贝壳平台会给出一个参考价，所以取最大值，
        # 而由于数字的ASC码是递增的，所以直接比较字符串大小就行
        data_dict['总价'] = max(
            pq_doc(
                '#beike > div.sellDetailPage > div:nth-child(6) > div.overview > div.content > div.price > span.total').text(),
            pq_doc(
                '#beike > div.sellDetailPage > div:nth-child(6) > div.overview > div.content >'
                ' div.priceBox > p:nth-child(1) > span').text()
        )

        data_dict['单价'] = max(
            pq_doc('#beike > div.sellDetailPage > div:nth-child(6) > div.overview > div.content > '
                   'div.price > div.text > div.unitPrice > span').text(),
            pq_doc('#beike > div.sellDetailPage > div:nth-child(6) > div.overview > div.content >'
                   ' div.priceBox > p:nth-child(2) > span').text()
        )
        data_dict['格局'] = pq_doc("#beike > div.sellDetailPage > div:nth-child(6) > div.overview > div.content > "
                                 "div.houseInfo > div.room > div.mainInfo").text()
        data_dict['面积'] = pq_doc('#beike > div.sellDetailPage > div:nth-child(6) > div.overview > '
                                 'div.content > div.houseInfo > div.area > div.mainInfo').text()
        data_dict['建成时间'] = pq_doc('#beike > div.sellDetailPage > div:nth-child(6) > div.overview > div.content >'
                                   ' div.houseInfo > div.area > div.subInfo.noHidden').text().split('\n')[0].strip()
        data_dict['信息来源'] = '贝壳二手房'
        data_dict['原网址'] = self.url

        # print(list(data_dict.values()))  # 此句是测试时使用，为了检测上述信息爬取是否正确
        self.q.put(list(data_dict.values()))


class Coodinate(Thread):
    """
    获取经纬度数据的多线程爬虫对象
    """

    def __init__(self, place, city, index, queue):
        super(Coodinate, self).__init__()
        self.place = place  # 地址信息
        self.index = index  # index代表在dataframe对象中的位置，因为多线程队列并不能自己保持顺序
        self.city = city
        self.queue = queue  # 这是一个Queue()对象

    def run(self):
        """
        对Thread方法中的run方法进行重载，通过此方法进行线程数量的控制
        :return:
        """
        global sem1  # 最大线程数，sem1是一个threading.Semaphore(int)对象
        with sem1:
            self.get_coodination()
            global count1
            count1 += 1
            if count1 % 100 == 0:
                print("已经处理{}条经纬度信息".format(count1))

    # 以下方法是将文字地址通过查询得到经纬度地址，同时将数据返回到队列queue中
    def get_coodination(self):
        self.queue.put(
            (add_coodinate_information.get_thecoodinate_information(self.place, self.city), self.index)
        )


class LianjiaSpider(Thread):
    """
        爬取链家的爬虫对象，这个类和BeikeSpider高度类似，就不重复写注释了
    """

    def __init__(self, url, city, q, proxy=None):
        super(LianjiaSpider, self).__init__()
        if proxy is None:
            proxy = {}
        self.url = url
        self.city = city
        self.q = q  # 这是一个Queue()对象
        self.proxies = proxy

    def run(self):
        with lianjia_sem:
            self.lianjia_parse_page()
            global lianjia_count
            lianjia_count += 1
            if lianjia_count % 100 == 0:
                print("已经处理{}条消息".format(lianjia_count))

    def lianjia_parse_page(self):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/87.0.4280.88 Safari/537.36 '
        }
        cookies = {'cookie':
                       "lianjia_uuid=dc17de0b-6062-434e-a691-92af1672d39a; "
                       "UM_distinctid=179b640ddf070-09c89cf367b585-51361244-144000-179b640ddf1dbe; _smt_uid=60b1ba97.5bbda357; "
                       "_ga=GA1.2.596646375.1622260377; Hm_lvt_9152f8221cb6243a53c83b956842be8a=1622260731; "
                       "lianjia_ssid=b42c1ca8-4716-4a50-a6b5-24356503e2e1; select_city=310000; _gid=GA1.2.1155027429.1622790220; "
                       "sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22179b640df91100d-0735549aeff647-51361244-1327104"
                       "-179b640df92cd3%22%2C%22%24device_id%22%3A%22179b640df91100d-0735549aeff647-51361244-1327104-179b640df92cd3"
                       "%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C"
                       "%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22"
                       "%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%7D; "
                       "srcid"
                       "=eyJ0Ijoie1wiZGF0YVwiOlwiNjBlYjg0NTEzYzhiYjdkYzM0YmUyNmQ0ZWI5ZWI2Mjg5Y2ZhMDkxMmZkYzczNTczYzBkNzdjNzdkOTQ5ZDEzNWM1YmZlYjk0NzAwNDZiZWUwZjRlMTQ0OTllZjBmNmQ2OWMyNTU5MjI0MTE3ODFhYWFiNjE0ZGNmZjhiNGQ0NjM5NWQxOGRkY2NlYjIwZTgxOGQwYzI5ZDk5NjU0NmQwNGMyMzMyMmU0ZWUyODdiODk2MzRmZWM3YTRlYjYzNjVkNjc1MGQwMDc0Y2Q1M2I2ZGUyNzdhNTEzNWViNmRhYjVjODUxMzNlY2E5ZGFjNmEzZmMzYzZiNzUyMzUwOTIxNjU4Njc3MDZiNGQ1MGVhY2Q4ZjM3OGQxZmI5ZmEzODE5YTBiMzM5MDViMTM0Yjc5NzUxY2FjMTNhMTU5MmUyMWVlN2QxZDI2NGUyZDA1MDQzNGQ4YzU5YTY2NGNkYWZkNFwiLFwia2V5X2lkXCI6XCIxXCIsXCJzaWduXCI6XCIyZmE4YmM5N1wifSIsInIiOiJodHRwczovL3NoLmxpYW5qaWEuY29tL2Vyc2hvdWZhbmcvcGcxMDAvIiwib3MiOiJ3ZWIiLCJ2IjoiMC4xIn0=; _gat=1; _gat_past=1; _gat_global=1; _gat_new_global=1; _gat_dianpu_agent=1 "
                   }
        # requests.packages.urllib3.disable_warnings()
        if self.proxies:
            resp = requests.get(self.url, headers=headers, cookies=cookies, proxies=self.proxies)
        else:
            resp = requests.get(self.url, headers=headers, cookies=cookies)
        resp_text = resp.text
        pq_doc = pq(resp_text)

        data_dict = dict()
        data_dict['所属城市'] = self.city
        # 逐个找到信息
        data_dict['地址'] = pq_doc(
            'body > div.overview > div.content > div.aroundInfo '
            '> div.areaName > span.info > a:nth-child(1)').text().strip() + \
                          pq_doc('body > div.overview > div.content > div.aroundInfo > '
                                 'div.communityName > a.info').text().strip()
        # 这里取两个的最大值是因为，有的房源房主并没有报价，贝壳平台会给出一个参考价，所以取最大值，
        # 而由于数字的ASC码是递增的，所以直接比较字符串大小就行
        data_dict['总价'] = max(
            pq_doc(
                'body > div.overview > div.content > div.price > span.total').text().strip(),
            pq_doc(
                'body > div.overview > div.content > div.priceBox > p:nth-child(1) > span').text().strip()[:-1]
            # 去掉“万”字
        )

        data_dict['单价'] = max(
            pq_doc('body > div.overview > div.content > div.price > div.text > div.unitPrice > span').text().strip(),
            pq_doc('body > div.overview > div.content > div.priceBox > p:nth-child(2) > span').text().strip()
        )
        data_dict['格局'] = pq_doc(
            "body > div.overview > div.content > div.houseInfo > div.room > div.mainInfo").text().strip()
        data_dict['面积'] = pq_doc(
            'body > div.overview > div.content > div.houseInfo > div.area > div.mainInfo').text().strip()
        data_dict['建成时间'] = \
            pq_doc('body > div.overview > div.content > div.houseInfo > div.area > div.subInfo.noHidden').text().split(
                '\n')[0].strip()
        data_dict['信息来源'] = '链家'
        data_dict['原网址'] = self.url

        self.q.put(list(data_dict.values()))


def beike_get_url(city='北京', proxy=None):
    """
    此函数用于爬取贝壳找房的房源信息网址集合，返回值为一个列表
    :return:一个元素为各房源的网址的列表
    """
    # 初始化程序窗口
    if proxy is None:
        proxy = {}
    options = Options()
    browser = webdriver.Chrome(options=options)
    browser.get('https://www.ke.com/city/')
    browser.maximize_window()

    # 在城市搜索中输入城市名，并单击“搜索”按钮跳转到指定的城市页面（此处通过按回车键来实现单击）
    text = browser.find_element_by_xpath('/html/body/div[2]/div[1]/div/input')
    text.clear()
    text.send_keys(city)
    time.sleep(1)
    text.send_keys(Keys.ENTER)

    # 切换到新的窗口
    browser.switch_to.window(browser.window_handles[1])

    # 直接单击房源搜索，跳转到房源列表
    text = browser.find_element_by_xpath('/html/body/div[1]/div/div[4]/div[2]/div/div[2]/div[1]/div[1]/input[3]')
    text.send_keys(Keys.ENTER)

    # 遍历第一页页面的房源信息
    url_list = []
    pq_doc1 = pq(browser.page_source)
    content_list = pq_doc1('#beike > div.sellListPage > div.content > div.leftContent > div:nth-child(4) > ul')
    for item in content_list.children('li'):
        pq1 = pq(item)
        if pq1('a').attr('href')[-4:] == 'html':
            url_list.append(pq1('a').attr('href'))
    print("每一页的房源信息条数为{}条".format(len(url_list)))

    # 为了保证能够在翻页到最后一页时退出，我们需要知道总页数
    # 总页数以Int形式储存在total_page中
    pq_doc1 = pq(browser.page_source)
    page_box_doc = pq_doc1(
        '#beike > div.sellListPage > div.content > div.leftContent > div.contentBottom.clear > div.page-box.fr > div')
    text_list = list()
    for item in page_box_doc.children('a'):
        pq2 = pq(item)
        text_list.append(pq2.text())
    total_page = 0
    for item in text_list:
        if item.isdigit():  # 排除非数字字符串
            if int(item) > total_page:
                total_page = int(item)
    print('{}房源信息一共有{}页'.format(city, total_page))

    # 获取第一页url以便接下来遍历使用，同时关闭browser
    first_page = browser.current_url
    time.sleep(1)
    browser.quit()

    # 接下来遍历剩余的所有页
    for i in range(total_page - 1):
        html = first_page[:-3] + 'pg{}/'.format(i + 2)
        print("正在获取第{}页的房源网址".format(i + 2))

        if proxy:
            content = requests.get(html, proxies=proxy).text
        else:
            content = requests.get(html).text

        pq_doc = pq(content)
        content_list = pq_doc('#beike > div.sellListPage > div.content > div.leftContent > div:nth-child(4) > ul')
        for item in content_list('li'):
            pq1 = pq(item)
            if pq1('a').attr('href') is not None and pq1('a').attr('href')[-4:] == 'html':
                url_list.append(pq1('a').attr('href'))
        del url_list[-1]  # 删除无关数据
        # 以下两行是为了测试网站能承受线程数时，只利用前几页数据进行测试使用
        # if i == 5:
        #     break
    print("{}在贝壳二手房上一共有{}条房源信息".format(city, len(url_list)))
    return url_list


def anjvke_get_url(city='北京'):
    """
    此函数用于爬取安居客的房源信息网址集合，返回值为一个列表
    :return:一个储存有安居客当前城市所有房源信息的二维列表
    """
    # 由于安居客不同城市的网址和城市的拼音有关，所以我们首先得到要搜索城市的拼音，进而得到网址
    # 这里用到pypinyin库
    c = ''  # 将城市名称转化为拼音之后的储存变量
    for i in pypinyin.pinyin(city, style=pypinyin.NORMAL):
        c += ''.join(i)

    options = Options()
    options.add_argument("--proxy-server=tps104.kdlapi.com:15818")  # 使用隧道代理
    browser = webdriver.Chrome(options=options)
    browser.get("https://beijing.anjuke.com/sale/p1/#")
    browser.maximize_window()
    input("验证完成后继续")  # 因为这里可能会出现拼图验证，需要手动验证
    resp = browser.page_source

    # 遍历第一页页面的房源信息
    house_list = []
    house_list.extend(anjvke_parse_page(city, resp))
    print("已经在安居客上找到{}条{}房源信息".format(len(house_list), city))

    # 接下来遍历剩余的所有页
    page_number = 2
    while page_number <= 50:
        html = "https://{}.anjuke.com/sale/p{}/?from=sugg".format(c, str(page_number))
        browser.get(html)
        content = browser.page_source
        pq_doc1 = pq(content)
        if pq_doc1('#ISDCaptcha > div.dvc-slider'):
            # 拼图验证会时不时出现，如果出现，则需要手动验证，并在跳转之后重新获取一次网页源代码
            input("完成验证后继续")
            content = browser.page_source
            house_list.extend(anjvke_parse_page(city, content))
            page_number += 1
            print("已经在安居客上找到{}条{}房源信息".format(len(house_list), city))
        else:
            house_list.extend(anjvke_parse_page(city, content))
            print("已经在安居客上找到{}条{}房源信息".format(len(house_list), city))
            page_number += 1
    print("一共在安居客上找到{}条{}房源信息".format(len(house_list), city))
    browser.quit()
    return house_list


def lianjia_get_url(city='北京'):
    """
        此函数用于爬取链家的房源信息网址集合，返回值为一个列表
        :return:一个元素为各房源的网址的列表
        """
    # 初始化程序窗口
    options = Options()
    options.add_argument(
        'user-agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"')
    browser = webdriver.Chrome(options=options)
    # browser.get('https://ipv4.ddnspod.com')  # 这一句测试代理是否成功时使用
    browser.get('https://www.lianjia.com/city/')
    browser.maximize_window()

    # 在城市搜索中输入城市名，并单击“搜索”按钮跳转到指定的城市页面（此处通过按回车键来实现单击）
    text = browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/input')
    text.clear()
    text.send_keys(city)
    time.sleep(1)
    text.send_keys(Keys.ENTER)

    # 切换到新的窗口
    browser.switch_to.window(browser.window_handles[1])

    # 直接单击房源搜索，跳转到房源列表
    text = browser.find_element_by_xpath('/html/body/div[1]/div/div[5]/div[3]/div/div[2]/div[1]/div[1]/input[1]')
    text.send_keys(Keys.ENTER)

    # 获取第一页url以便接下来遍历使用，同时关闭browser
    first_page = browser.current_url
    time.sleep(1)
    browser.quit()

    return first_page[:-3]


def anjvke_parse_page(city, raw_html):
    """
    此方法用来从安居客网站上找到特定的房源信息
    """
    data_dict = dict()
    data_dict['所属城市'] = city

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


def Lianjia(city='北京', proxy=None):
    """
    此函数用于爬取链家的房源信息，使用时直接调用此函数就可以爬取链家的房源信息
    :param city: 城市名
    :param proxy: 网络代理，格式为requests.get()方法中的proxies关键字格式
    :return: 无返回值
    """
    if proxy is None:
        proxy = {}
    print('正在获取链家{}的房源数据……'.format(city))
    main_part = lianjia_get_url(city)
    url_list = [main_part + 'pg{}/'.format(i) for i in range(1, 101)]
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/87.0.4280.88 Safari/537.36 '
    }
    cookies = {'cookie':
                   "lianjia_uuid=dc17de0b-6062-434e-a691-92af1672d39a; "
                   "UM_distinctid=179b640ddf070-09c89cf367b585-51361244-144000-179b640ddf1dbe; _smt_uid=60b1ba97.5bbda357; "
                   "_ga=GA1.2.596646375.1622260377; Hm_lvt_9152f8221cb6243a53c83b956842be8a=1622260731; "
                   "lianjia_ssid=b42c1ca8-4716-4a50-a6b5-24356503e2e1; select_city=310000; _gid=GA1.2.1155027429.1622790220; "
                   "sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22179b640df91100d-0735549aeff647-51361244-1327104"
                   "-179b640df92cd3%22%2C%22%24device_id%22%3A%22179b640df91100d-0735549aeff647-51361244-1327104-179b640df92cd3"
                   "%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C"
                   "%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22"
                   "%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%7D; "
                   "srcid"
                   "=eyJ0Ijoie1wiZGF0YVwiOlwiNjBlYjg0NTEzYzhiYjdkYzM0YmUyNmQ0ZWI5ZWI2Mjg5Y2ZhMDkxMmZkYzczNTczYzBkNzdjNzdkOTQ5ZDEzNWM1YmZlYjk0NzAwNDZiZWUwZjRlMTQ0OTllZjBmNmQ2OWMyNTU5MjI0MTE3ODFhYWFiNjE0ZGNmZjhiNGQ0NjM5NWQxOGRkY2NlYjIwZTgxOGQwYzI5ZDk5NjU0NmQwNGMyMzMyMmU0ZWUyODdiODk2MzRmZWM3YTRlYjYzNjVkNjc1MGQwMDc0Y2Q1M2I2ZGUyNzdhNTEzNWViNmRhYjVjODUxMzNlY2E5ZGFjNmEzZmMzYzZiNzUyMzUwOTIxNjU4Njc3MDZiNGQ1MGVhY2Q4ZjM3OGQxZmI5ZmEzODE5YTBiMzM5MDViMTM0Yjc5NzUxY2FjMTNhMTU5MmUyMWVlN2QxZDI2NGUyZDA1MDQzNGQ4YzU5YTY2NGNkYWZkNFwiLFwia2V5X2lkXCI6XCIxXCIsXCJzaWduXCI6XCIyZmE4YmM5N1wifSIsInIiOiJodHRwczovL3NoLmxpYW5qaWEuY29tL2Vyc2hvdWZhbmcvcGcxMDAvIiwib3MiOiJ3ZWIiLCJ2IjoiMC4xIn0=; _gat=1; _gat_past=1; _gat_global=1; _gat_new_global=1; _gat_dianpu_agent=1 "
               }
    # 以下这条语句是用来测试隧道代理是否成功
    # print(requests.get('https://ipv4.ddnspod.com/', proxies=proxy).text)

    house_url_list = []
    for page_url in url_list:
        if proxy:
            resp = requests.get(page_url, headers=headers, cookies=cookies, proxies=proxy)
        else:
            resp = requests.get(page_url, headers=headers, cookies=cookies)
        resp_text = resp.text
        pq_doc = pq(resp_text)  # 创建pyquery对象

        # content_list是房源信息的列表框
        content_list = pq_doc('#content > div.leftContent > ul')
        for item in content_list.children('li'):
            pq1 = pq(item)
            if pq1('a').attr('href')[-4:] == 'html':
                house_url_list.append(pq1('a').attr('href'))
        print("已经在链家找到{}条{}的房源信息".format(len(house_url_list), city))

    # 创建一个队列用于保存线程获取到的所有数据
    q = Queue()

    # 保存线程
    Thread_list = list()

    # 创建并启动线程
    global lianjia_sem  # 最大活跃线程数量
    lianjia_sem = threading.Semaphore(10)
    global lianjia_count  # 统计已经处理的链家房源数量
    lianjia_count = 0
    for url in house_url_list:
        p = LianjiaSpider(url, city, q, proxy)
        p.start()  # 启用多线程
        Thread_list.append(p)

    # 让主线程等待子线程执行完成
    for thread in Thread_list:
        thread.join()

    temp_list1 = list()  # 用于将q中数据导出到dataframe的中间存储变量
    while not q.empty():
        temp_list1.append(q.get())
    # 创建DataFrame对象
    lianjia_df = add_coodinate_information.make_dataframe(temp_list1)
    del temp_list1

    # 添加经纬度地址
    print('开始查找链家经纬度地址')
    lianjia_df['经纬度'] = [''] * len(lianjia_df)
    q1 = Queue()  # 队列对象，用于多线程加速获取经纬度信息
    Thread_list1 = list()
    global sem1
    sem1 = threading.Semaphore(8)
    global count1
    count1 = 0
    for i in range(len(lianjia_df['地址'])):
        p = Coodinate(lianjia_df['地址'][i], city, i, q1)
        p.start()
        Thread_list1.append(p)

    # 让主线程等待子线程执行完成
    for thread in Thread_list1:
        thread.join()

    # 将经纬度地址信息从队列中保存到dataFrame对象中
    while not q1.empty():
        temp_tuple = q1.get()
        lianjia_df['经纬度'][temp_tuple[1]] = temp_tuple[0]

    print('正在写入数据库……')
    add_coodinate_information.save_to_mysql(lianjia_df, '_Lianjia_{}{}'.format(city, time.strftime("%Y-%m-%d_%H:%M:%S",
                                                                                                   time.localtime())))
    print('成功将_Lianjia_{}{}写入数据库'.format(city, time.strftime("%Y-%m-%d_%H:%M:%S", time.localtime())))


def Beike(city='北京', proxy=None):
    """
    此函数用于爬取贝壳二手房的信息，只需调用此函数便可获取制定城市在贝壳二手房上的所有二手房信息
    :param city: 城市名
    :param proxy: 网络代理，格式为requests.get()方法中的proxies关键字格式
    :return: 无返回值
    """
    # 贝壳二手房
    if proxy is None:
        proxy = {}
    print('正在获取贝壳二手房{}的房源数据……'.format(city))
    if proxy:
        beike_url_list = beike_get_url(city)  # 贝壳二手房房源url列表
    else:
        beike_url_list = beike_get_url(city)  # 贝壳二手房房源url列表

    # 创建一个队列用于保存线程获取到的所有数据
    q = Queue()

    # 保存线程
    Thread_list = list()

    # 创建并启动线程
    global beike_sem  # 最大活跃线程数量
    beike_sem = threading.Semaphore(10)
    global beike_count  # 统计已经处理过的房源信息数量
    beike_count = 0
    for url in beike_url_list:
        p = BeikeSpider(url, city, q)
        p.start()
        Thread_list.append(p)

    # 让主线程等待子线程执行完成
    for thread in Thread_list:
        thread.join()

    temp_list1 = list()  # 用于将q中数据导出到dataframe的中间存储变量
    while not q.empty():
        temp_list1.append(q.get())

    # 创建DataFrame对象
    beike_df = add_coodinate_information.make_dataframe(temp_list1)
    del temp_list1

    # 添加经纬度地址
    print('开始查找经纬度地址')
    beike_df['经纬度'] = [''] * len(beike_df)
    q1 = Queue()
    Thread_list1 = list()
    global sem1
    sem1 = threading.Semaphore(8)
    global count1
    count1 = 0
    for i in range(len(beike_df['地址'])):
        p = Coodinate(beike_df['地址'][i], city, i, q1)
        p.start()
        Thread_list1.append(p)

    # 让主线程等待子线程执行完成
    for thread in Thread_list1:
        thread.join()

    while not q1.empty():
        temp_tuple = q1.get()
        beike_df['经纬度'][temp_tuple[1]] = temp_tuple[0]

    print('正在写入数据库……')
    add_coodinate_information.save_to_mysql(beike_df, '_Beike_{}{}'.format(city, time.strftime("%Y-%m-%d_%H:%M:%S",
                                                                                               time.localtime())))
    print('成功将_Beike_{}{}写入数据库'.format(city, time.strftime("%Y-%m-%d_%H:%M:%S", time.localtime())))


def Anjvke(city='北京'):
    """
    此函数用于爬取安居客的二手房信息，调用此函数就能获得指定城市在安居客上的所有二手房信息
    :param city: 城市名
    :return: 无返回值
    """
    print("正在获取{}安居客房源信息".format(city))
    anjvke_url_list = anjvke_get_url(city)  # 安居客房源url列表

    anjvke_df = add_coodinate_information.make_dataframe(anjvke_url_list)

    # 添加经纬度地址
    print('开始查找经纬度地址')
    anjvke_df['经纬度'] = [''] * len(anjvke_df)
    q1 = Queue()
    Thread_list1 = list()
    global sem1
    sem1 = threading.Semaphore(8)
    global count1
    count1 = 0
    for i in range(len(anjvke_df['地址'])):
        p = Coodinate(anjvke_df['地址'][i], city, i, q1)
        p.start()
        Thread_list1.append(p)

    # 让主线程等待子线程执行完成
    for thread in Thread_list1:
        thread.join()

    while not q1.empty():
        temp_tuple = q1.get()
        anjvke_df['经纬度'][temp_tuple[1]] = temp_tuple[0]

    print('正在写入数据库……')
    add_coodinate_information.save_to_mysql(anjvke_df, '_Anjvke_{}{}'.format(city, time.strftime("%Y-%m-%d_%H:%M:%S",
                                                                                                 time.localtime())))
    print('成功将_Anjvke_{}{}写入数据库'.format(city, time.strftime("%Y-%m-%d_%H:%M:%S", time.localtime())))


if __name__ == '__main__':
    """
    以下内容主要用于编写程序测试时使用
    """
    tunnel = "tps104.kdlapi.com:15818"
    username = "t12286606203573"
    password = "7eawun21"
    proxy = {
        "http": "http://%(user)s:%(pwd)s@%(proxy)s/" % {"user": username, "pwd": password, "proxy": tunnel},
        "https": "http://%(user)s:%(pwd)s@%(proxy)s/" % {"user": username, "pwd": password, "proxy": tunnel}
    }
    Anjvke()
