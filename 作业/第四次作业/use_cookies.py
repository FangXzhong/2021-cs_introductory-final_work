import json
import time
from pyquery import PyQuery as Pq
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def use_zhihu_cookies():
    """
    这个函数使用了保存好的cookies，并在登录完成后截屏以确认登录成功
    :return:函数会返回一个浏览器对象browser
    """
    options = Options()
    # options.add_argument("--headless")  # 不打开浏览器界面，以节省时间
    browser = webdriver.Chrome(options=options)

    # 先建立连接, 随后才可以可修改cookie
    browser.get('https://www.zhihu.com/signin?next=%2F')
    browser.maximize_window()
    # 删除这次登录时，浏览器自动储存到本地的cookie
    browser.delete_all_cookies()

    # 读取之前已经储存到本地的cookie
    cookies_filename = './data/my_cookies.json'
    cookies_file = open(cookies_filename, 'r', encoding='utf-8')
    cookies_list = json.loads(cookies_file.read())

    for cookie in cookies_list:
        browser.add_cookie({
            'domain': '.zhihu.com',
            'name': cookie['name'],
            'value': cookie['value'],
            'path': '/',
            'expires': None
        })

    browser.get("https://www.zhihu.com/signin?next=%2F")
    time.sleep(3)

    browser.save_screenshot("./output/zhihu_login.png")
    return browser


def save_the_html(browser):
    """
    这个函数用来跳转到知乎热榜界面并将页面保存到本地以便后续操作
    :param browser: 浏览器页面对象
    :return:
    """
    # 找到“热榜”按钮
    button1_selector = '#root > div > main > div > div > div.Topstory-mainColumn ' \
                       '> div > div.Card.Topstory-noMarginCard.Topstory-tabCard > nav > a:nth-child(3)'
    button1 = browser.find_element_by_css_selector(button1_selector)
    button1.click()
    time.sleep(5)
    html1 = browser.page_source
    f = open('a.html', 'w', encoding='utf8')
    f.write(html1)
    f.close()
    browser.close()


def get_the_hotpoint(filename):
    """
    这个函数读入保存到本地的html文件，同时提取知乎热榜的标题和热度
    :param filename: 保存在本地的html文件
    :return:返回一个列表，列表中的元素是[序号，标题名，热度]——即返回的是一个二维列表
    """
    final_list = list()

    f = open(filename, 'r', encoding="utf8")
    d = Pq(f.read())
    f.close()

    hotlist = d("#TopstoryContent > div > div > div.HotList-list")
    pq_items = hotlist('section')
    item_list = pq_items.items()

    rank = 1
    for item in item_list:
        title = item('a').attr('title')
        raw_text = item('div.HotItem-content div').text()
        after_text = raw_text.split("\n")[0]
        final_list.append([rank, title, after_text])
        rank += 1
    print(final_list)
    return final_list


def save_the_hotpoint(data):
    """
    这个函数用来将热度内容进行保存
    :param data: 是一个二维列表，列表元素为[序号(int)，标题名(str)，热度值(str)]
    :return: 无返回值
    """
    f = open("./output/hotpoint.csv", 'w', encoding="gb18030")
    f.write("序号,标题,热度值\n")
    for i in range(len(data)):
        data[i][0] = str(data[i][0])
        f.write(','.join(data[i])+'\n')
    f.close()


if __name__ == '__main__':
    browser1 = use_zhihu_cookies()
    save_the_html(browser1)
    hot_list = get_the_hotpoint('a.html')
    save_the_hotpoint(hot_list)
