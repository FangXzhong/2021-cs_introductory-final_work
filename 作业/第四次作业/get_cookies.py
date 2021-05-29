import json
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def get_zhihu_cookies():
    """
    这个函数用来获取并保存cookies，运行之后会将cookies保存到./data/my_cookies.json中
    :return: 无
    """
    options = Options()
    browser = webdriver.Chrome(options=options)
    browser.get('https://www.zhihu.com/signin?next=%2F')
    browser.maximize_window()

    input("请用手机扫码登录，然后按回车……")  # 等待用手机扫码登录, 登录后回车即可

    cookies_dict = browser.get_cookies()
    cookies_json = json.dumps(cookies_dict)
    print(cookies_json)

    # 登录完成后,将cookies保存到本地文件
    out_filename = './data/my_cookies.json'
    out_file = open(out_filename, 'w', encoding='utf-8')
    out_file.write(cookies_json)
    out_file.close()
    print('Cookies文件已写入：' + out_filename)

    browser.quit()


if __name__ == '__main__':
    get_zhihu_cookies()
