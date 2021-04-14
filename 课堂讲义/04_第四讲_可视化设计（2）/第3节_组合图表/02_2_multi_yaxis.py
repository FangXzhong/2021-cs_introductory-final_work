"""
Date: 2021.3.22
Author: Justin

要点说明：
绘制柱状图，包含两个不同的Y轴
基于pyecharts官方文档示例修改
"""

from pyecharts.faker import Faker
from pyecharts import options as opts
from pyecharts.charts import Bar, Grid, Line, Scatter


x_data = ["{}月".format(i) for i in range(1, 13)]

bar = (
    Bar()
    .add_xaxis(x_data)
    .add_yaxis(
        "蒸发量",
        [2.0, 4.9, 7.0, 23.2, 25.6, 76.7, 135.6, 162.2, 32.6, 20.0, 6.4, 3.3],
        yaxis_index=0,
        color="#d14a61",
    )
    .add_yaxis(
        "降水量",
        [2.6, 5.9, 9.0, 26.4, 28.7, 70.7, 175.6, 182.2, 48.7, 18.8, 6.0, 2.3],
        yaxis_index=1,
        color="#5793f3",
    )
    .extend_axis(
        yaxis=opts.AxisOpts(
            name="蒸发量",
            type_="value",
            min_=0,
            max_=250,
            position="right",
            axisline_opts=opts.AxisLineOpts(
                linestyle_opts=opts.LineStyleOpts(color="#d14a61")
            ),
            axislabel_opts=opts.LabelOpts(formatter="{value} ml"),
        )
    )
    .extend_axis(
        yaxis=opts.AxisOpts(
            type_="value",
            name="温度",
            min_=0,
            max_=25,
            position="left",
            axisline_opts=opts.AxisLineOpts(
                linestyle_opts=opts.LineStyleOpts(color="#675bba")
            ),
            axislabel_opts=opts.LabelOpts(formatter="{value} °C"),
            splitline_opts=opts.SplitLineOpts(
                is_show=True, linestyle_opts=opts.LineStyleOpts(opacity=1)
            ),
        )
    )
    .set_global_opts(
        yaxis_opts=opts.AxisOpts(
            name="降水量",
            min_=0,
            max_=250,
            position="right",
            offset=80,#Y 轴相对于默认位置的偏移，在相同的 position 上有多个 Y 轴的时候有用
            axisline_opts=opts.AxisLineOpts(
                linestyle_opts=opts.LineStyleOpts(color="#5793f3")
            ),
            axislabel_opts=opts.LabelOpts(formatter="{value} ml"),
        ),
        title_opts=opts.TitleOpts(title="多Y轴示例"),
        tooltip_opts=opts.TooltipOpts(trigger="axis", axis_pointer_type="cross"),#提示框配置项
    )
)

bar.render('./output/grid_mult_yaxis.html')