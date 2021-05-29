import time
import pypinyin
import requests
from pyquery import PyQuery as pq
from selenium import webdriver
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
    pass


if __name__ == '__main__':
    function1()
