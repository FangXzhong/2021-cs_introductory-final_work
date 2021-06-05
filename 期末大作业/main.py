"""
    Author:Fang Xiangz
    Date:2021.5.30
    这个是主程序，运行这个即可
"""
import get_the_raw_information

if __name__ == '__main__':
    city_list = ['上海', '深圳', '北京', ]
    for city in city_list:
        get_the_raw_information.Beike(city=city)
        get_the_raw_information.Lianjia(city)
        get_the_raw_information.Anjvke(city)
        break
