"""
    首先，我们需要爬取贝壳找房、房多多和安居客网站上的房源信息，每一条房源信息的格式为
    [所属城市,地址,总价,单价,格局,面积,建成时间,信息来源,原网址]
"""
import time
import pypinyin
import requests
from pyquery import PyQuery as pq
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options


def beike_get_url(city='北京'):
    """
    此函数用于爬取贝壳找房的房源信息网址集合，返回值为一个列表
    :return:一个元素为各房源的网址的列表
    """
    # 初始化程序窗口
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
    print(len(url_list))

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
        if item.isdigit():
            if int(item) > total_page:
                total_page = int(item)
    print(total_page)

    # 获取第一页url以便接下来遍历使用，同时关闭browser
    first_page = browser.current_url
    time.sleep(1)
    browser.quit()

    # 接下来遍历剩余的所有页
    for i in range(total_page - 1):
        html = first_page[:-3] + 'pg{}/'.format(i + 2)
        print(html)
        content = requests.get(html).text
        pq_doc = pq(content)
        content_list = pq_doc('#beike > div.sellListPage > div.content > div.leftContent > div:nth-child(4) > ul')
        for item in content_list('li'):
            pq1 = pq(item)
            if pq1('a').attr('href') is not None and pq1('a').attr('href')[-4:] == 'html':
                url_list.append(pq1('a').attr('href'))
        del url_list[-1]
        # break
    print(len(url_list))
    return url_list


def beike_get_information(city='北京', url='https://bj.ke.com/ershoufang/101111224667.html'):
    """
    此函数用来从网站上找到特定的房源信息
    :param city: 所属城市
    :param url: 房源详情网址
    :return: [所属城市,地址,总价,单价,格局,面积,建成时间,信息来源,原网址]
    """
    data_dict = dict()
    data_dict['所属城市'] = city

    # 获取页面源代码
    raw_html = requests.get(url).text
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
    data_dict['总价'] = pq_doc(
        '#beike > div.sellDetailPage > div:nth-child(6) > div.overview > div.content > div.price > span.total').text()
    data_dict['单价'] = pq_doc('#beike > div.sellDetailPage > div:nth-child(6) > div.overview > div.content > '
                             'div.price > div.text > div.unitPrice > span').text()
    data_dict['格局'] = pq_doc("#beike > div.sellDetailPage > div:nth-child(6) > div.overview > div.content > "
                             "div.houseInfo > div.room > div.mainInfo").text()
    data_dict['面积'] = pq_doc('#beike > div.sellDetailPage > div:nth-child(6) > div.overview > '
                             'div.content > div.houseInfo > div.area > div.mainInfo').text()
    data_dict['建成时间'] = pq_doc('#beike > div.sellDetailPage > div:nth-child(6) > div.overview > div.content >'
                               ' div.houseInfo > div.area > div.subInfo.noHidden').text().split('\n')[0].strip()
    data_dict['信息来源'] = '贝壳二手房'
    data_dict['原网址'] = url
    return list(data_dict.values())


def anjvke_get_url(city='北京'):
    """
    此函数用于爬取安居客的房源信息网址集合，返回值为一个列表
    :return:一个元素为各房源的网址的列表
    """
    # 由于安居客不同城市的网址和城市的拼音有关，所以我们首先得到要搜索城市的拼音，进而得到网址
    c = ''
    for i in pypinyin.pinyin(city, style=pypinyin.NORMAL):
        c += ''.join(i)

    # 初始化程序窗口
    chrome_options = Options()
    chrome_options.add_argument(
        'user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'
        ' Chrome/86.0.4240.75 Safari/537.36')
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    chrome_options.add_experimental_option('excludeSwitches', ['enable-automation'])
    browser = webdriver.Chrome(options=chrome_options)
    browser.get('https://{}.anjuke.com/sale/rd1/?kw=&from=sugg'.format(c))
    browser.maximize_window()
    input('此处可能有拼图验证')

    # # 直接单击房源搜索，跳转到房源列表
    # text = browser.find_element_by_xpath('/html/body/div[2]/div[2]/div[1]/div[1]/div/div[2]/form[2]/div/a[1]/input')
    # text.send_keys(Keys.ENTER)
    # input("验证过后，单击回车")

    # 遍历第一页页面的房源信息
    url_list = []
    pq_doc1 = pq(browser.page_source)
    content_list = pq_doc1('#__layout > div > section > section.list-main > section.list-left > section:nth-child(4)')
    for item in content_list.children('div'):
        pq1 = pq(item)
        url_list.append(pq1('a').attr('href'))
    print(len(url_list))

    # 获取第一页url以便接下来遍历使用，同时关闭browser
    first_page = browser.current_url
    time.sleep(1)
    browser.quit()

    # 接下来遍历剩余的所有页
    flag = 1
    page_number = 2
    while flag:
        html = 'https://{}.anjuke.com/sale/p{}/?from=sugg'.format(city, str(page_number))
        print(html)
        content = requests.get(html).text
        pq_doc1 = pq(content)
        content_list = pq_doc1(
            '#__layout > div > section > section.list-main > section.list-left > section:nth-child(4)')
        for item in content_list.children('div'):
            pq1 = pq(item)
            url_list.append(pq1('a').attr('href'))
        page_number += 1
        # 此处要判断是不是最后一页，如果是，终止循环
        pagination_doc = pq_doc1('#__layout > div > section > section.list-main > '
                                 'section.list-left > section.pagination-wrap > div')
        bs = BeautifulSoup(str(pagination_doc))
        for item in bs.find_all("a"):
            if item.text != "下一页":
                continue
            # 定位到“下一页”按钮，如果按不下去，就是最后一页
            print(item)
            if 'forbid' in str(''.join(item['class'])):
                print("最后一页！")
                flag = 0
    print(len(url_list))
    return url_list


def fangduoduo():
    """
    此函数用于爬取房多多的房源信息
    :return:
    """
    pass


if __name__ == '__main__':
    """
    以下内容主要用于编写程序测试时使用
    """
    # list1 = beike_get_url()  # 接收所有房源网址
    # list2 = list()  # 接收所有房源信息
    # count = 0
    # for item in list1:
    #     if count % 10 == 0:
    #         print('已经处理{}条信息'.format(count))
    #     list2.append(beike_get_information('北京', url=item))
    #     count += 1
    # print(list2)
    # f = open('1.csv', 'w', encoding='utf8')
    # for item in list2:
    #     f.write(",".join(item) + '\n')
    # f.close()

    # anjvke_get_url()
