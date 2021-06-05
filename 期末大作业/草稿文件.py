import threading
import time
import pymysql
import pandas as pd
import add_coodinate_information
import requests
import json
from sqlalchemy import create_engine
import pypinyin
import requests
from pyquery import PyQuery as pq
from selenium import webdriver
from bs4 import BeautifulSoup
from threading import Thread
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from multiprocessing import Process, Queue

import add_coodinate_information
import get_the_raw_information


def function1(city="北京"):
    # 由于安居客不同城市的网址和城市的拼音有关，所以我们首先得到要搜索城市的拼音，进而得到网址
    c = ''
    for i in pypinyin.pinyin(city, style=pypinyin.NORMAL):
        c += ''.join(i)

    options = Options()
    browser = webdriver.Chrome(options=options)
    browser.get('https://{}.anjuke.com/'.format(c))
    browser.maximize_window()


def function2():
    f = open('2.html', 'r', encoding="utf8")
    pq_doc = pq(f.read())
    pagination_doc = pq_doc('#__layout > div > section > section.list-main > '
                            'section.list-left > section.pagination-wrap > div')
    bs = BeautifulSoup(str(pagination_doc), 'lxml')
    flag = 1
    while flag:
        print('in while')
        for item in bs.find_all("a"):
            if item.text != "下一页":
                continue
            # 定位到“下一页”按钮，如果按不下去，就是最后一页
            print(item)
            if 'forbid' in str(''.join(item['class'])):
                print("over!")
                flag = 0


def function3():
    engine = create_engine('mysql+pymysql://final_homework:3JP387Rjs6e8ifWE@8.136.117.159:3306/final_homework')
    sql_query = 'SELECT * FROM `_Lianjia_北京2021-06-05_13:08:46`'
    df_read = pd.read_sql_query(sql_query, engine)
    df_read['经纬度'] = [add_coodinate_information.get_thecoodinate_information(item, '北京') for item in df_read['地址']]
    add_coodinate_information.save_to_mysql(df_read, sub_data='new_Lianjia_北京2021-06-05_13:08:46')


def function4():
    city_list = ['北京', '上海', '深圳']
    for city in city_list:

        # 贝壳二手房
        beike_url_list = get_the_raw_information.beike_get_url(city)  # 贝壳二手房房源url列表
        beike_house_list = list()  # 贝壳二手房房源信息列表
        count = 0
        for house_url in beike_url_list:
            if count % 10 == 0:
                print('已经处理{}条信息'.format(count))
            beike_house_list.append(get_the_raw_information.beike_get_information(city, url=house_url))
            count += 1

        # 创建DataFrame对象
        beike_df = add_coodinate_information.make_dataframe(beike_house_list)

        # 保存到数据库
        beike_df['经纬度'] = [add_coodinate_information.get_thecoodinate_information(item, city) for item in
                           beike_df['地址']]
        add_coodinate_information.save_to_mysql(beike_df, 'test_multiBeijing')
        break


def function5():
    get_the_raw_information.anjvke_get_url()


def function6():
    class test(Thread):
        def __init__(self):
            super(test, self).__init__()
            print("新的线程创建了")

        def run(self):
            self.god()

        def god(self):
            print("开始运行")

    with threading.Semaphore(2):
        for i in range(10):
            a = test()
            a.run()


def function7():
    param = {'orderid': "902286606202385", 'num': 1}
    resp = requests.get('http://tps.kdlapi.com/api/gettps', params=param)
    print(resp.text)
    proxy_ip = 'http://' + resp.text
    proxy_ips = 'https://' + resp.text

    tunnel = "tps104.kdlapi.com:15818"
    username = "t12286606203573"
    password = "7eawun21"
    proxy = {
        "http": "http://%(user)s:%(pwd)s@%(proxy)s/" % {"user": username, "pwd": password, "proxy": tunnel},
        "https": "http://%(user)s:%(pwd)s@%(proxy)s/" % {"user": username, "pwd": password, "proxy": tunnel}
    }
    # resp1 = requests.get('http://ipv4.ddnspod.com', proxies=proxy)
    # print(resp1.text)
    options = Options()
    options.add_argument("--proxy-server=tps104.kdlapi.com:15818")
    browser = webdriver.Chrome(options=options)
    browser.get("https://beijing.anjuke.com/sale/p1/#")
    browser.maximize_window()


if __name__ == '__main__':
    function7()
