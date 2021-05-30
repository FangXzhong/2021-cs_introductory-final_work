"""
    Author:Fang Xiangz
    Date:2021.5.30
    这个是主程序，运行这个即可
"""
import get_the_raw_information
import add_coodinate_information

if __name__ == '__main__':
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
        beike_df = add_coodinate_information.make_dataFrame(beike_house_list)

        # 保存到数据库
        add_coodinate_information.save_to_mysql(beike_df, 'test1')
        break
