import time
import pypinyin
import requests
from pyquery import PyQuery as pq
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options


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


if __name__ == '__main__':
    function2()
