"""
    该文件分为两大部分。
    第一部分利用高德地图来获取每个房源信息的经纬度坐标，以供后续可视化使用；
    第二部分将数据存储到MySQL数据库中
"""
import pandas as pd
import requests
import json
from sqlalchemy import create_engine


def function1():
    """
    这个函数是测试用的，不用管
    :return:
    """
    # 将数据从csv读取，并存入df中
    f = open('1.csv', 'r', encoding="utf8")
    list1 = list()
    for item in f.readlines():
        list1.append(item.strip().split(','))
    f.close()
    print(list1)
    df = pd.DataFrame(list1, index=list(range(len(list1))),
                      columns=['所属城市', '地址', '总价', '单价', '格局', '面积', '建成时间', '信息来源', '原网址'])
    print(df)
    df['经纬度'] = [get_thecoodinate_information(item) for item in df['地址']]
    print(df)
    save_to_mysql(df, sub_data='test1')


def save_to_mysql(df, sub_data='testdf'):
    # 存储到远程MySQL中
    engine = create_engine('mysql+pymysql://final_homework:3JP387Rjs6e8ifWE@8.136.117.159:3306/final_homework')
    df.to_sql(sub_data, engine)


def get_thecoodinate_information(place: str, city: str = '北京'):
    """
    通过高德地图获取经纬度坐标
    :return:
    """
    key = '87c8fc28a81f85c1092022c12566059f'
    url = 'https://restapi.amap.com/v3/geocode/geo'
    params = {'key': key, 'address': place, 'city': city}
    res = requests.get(url, params)
    json_data = json.loads(res.text)
    return json_data['geocodes'][0]['location']


def make_dataFrame(list1: list):
    df = pd.DataFrame(list1, index=list(range(len(list1))),
                      columns=['所属城市', '地址', '总价', '单价', '格局', '面积', '建成时间', '信息来源', '原网址'])
    return df
