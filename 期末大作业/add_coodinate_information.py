"""
    该文件分为两大部分。
    第一部分利用高德地图来获取每个房源信息的经纬度坐标，以供后续可视化使用；
    第二部分将数据存储到MySQL数据库中
"""
import pandas as pd
import time
import requests
import urllib3
import json
from sqlalchemy import create_engine


def function1():
    """
    这个函数是测试用的，不用管
    :return:
    """
    # 将数据从csv读取，并存入df中
    f = open('beike_df.csv', 'r', encoding="utf8")
    list1 = list()
    for item in f.readlines():
        list1.append(item.strip().split(','))
    f.close()
    print(list1)
    df = pd.DataFrame(list1, index=list(range(len(list1))),
                      columns=['index', '所属城市', '地址', '总价', '单价', '格局', '面积', '建成时间', '信息来源', '原网址'])
    # print(df)
    # df['经纬度'] = [get_thecoodinate_information(item) for item in df['地址']]
    # print(df)
    save_to_mysql(df, sub_data='test1')


def save_to_mysql(df, sub_data='testdf'):
    """存储到远程MySQL中"""
    engine = create_engine('mysql+pymysql://final_homework:3JP387Rjs6e8ifWE@8.136.117.159:3306/final_homework')
    df.to_sql(sub_data, engine)


def get_thecoodinate_information(place: str, city: str = '北京'):
    """
    通过高德地图获取经纬度坐标
    :return:经纬度坐标(str)，如果查询失败则返回NULL或者‘0,0’
    """
    # 先设定好要传递的参数
    key = '87c8fc28a81f85c1092022c12566059f'
    url = 'https://restapi.amap.com/v3/geocode/geo'
    params = {'key': key, 'address': place, 'city': city}

    requests.DEFAULT_RETRIES = 5  # 增加重试连接次数
    s = requests.session()
    s.keep_alive = False  # 关闭多余连接

    json_data = {}

    try:
        res = requests.get(url, params)
        json_data = json.loads(res.text)
    except requests.exceptions.ConnectionError or urllib3.exceptions.MaxRetryError:
        print('继续')
        time.sleep(1)

    # 以下是获取返回的json列表中的经纬度数据，为了应对因网络等原因导致的返回错误，所以就逐步筛选
    # 直到确认json_data['goecodes'][0]['location']存在后，获取该经纬度坐标
    if json_data:
        if 'geocodes' in dict(json_data).keys():
            if json_data['geocodes']:
                return json_data['geocodes'][0]['location']
        else:
            return '0,0'


def make_dataframe(list1: list):
    """
    这个函数用来将存储房源信息的二维列表转化为一个DataFrame对象，并将这个对象作为函数返回值返回
    :param list1: 存储有房源信息的二维列表
    :return: DataFrame对象
    """
    df = pd.DataFrame(list1, index=list(range(len(list1))),
                      columns=['所属城市', '地址', '总价', '单价', '格局', '面积', '建成时间', '信息来源', '原网址'])
    return df
