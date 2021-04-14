# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 12:22:05 2020
@author: Justin
"""
'''
Bar-添加y轴数值的函数定义
https://pyecharts.org/#/zh-cn/rectangular_charts?id=bar%EF%BC%9A%E6%9F%B1%E7%8A%B6%E5%9B%BE%E6%9D%A1%E5%BD%A2%E5%9B%BE

来自pyecharts 官方文档

后续的程序示例中，会挑选其中几个常用的参数，进行设置和演示
'''
def add_yaxis(
    # 系列名称，用于 tooltip 的显示，legend 的图例筛选。
    series_name: str,

    # 系列数据  
    y_axis: Sequence[Numeric, opts.BarItem, dict],

    # √ 是否选中图例
    is_selected: bool = True,

    # 使用的 x 轴的 index，在单个图表实例中存在多个 x 轴的时候有用。
    xaxis_index: Optional[Numeric] = None,

    # 使用的 y 轴的 index，在单个图表实例中存在多个 y 轴的时候有用。
    yaxis_index: Optional[Numeric] = None,

    # 系列 label 颜色
    color: Optional[str] = None,

    # √ 数据堆叠，同个类目轴上系列配置相同的　stack　值可以堆叠放置。 
    stack: Optional[str] = None,

    # 同一系列的柱间距离，默认为类目间距的 20%，可设固定值
    category_gap: Union[Numeric, str] = "20%",

    # 不同系列的柱间距离，为百分比（如 '30%'，表示柱子宽度的 30%）。
    # 如果想要两个系列的柱子重叠，可以设置 gap 为 '-100%'。这在用柱子做背景的时候有用。
    gap: Optional[str] = None,

    # 标签配置项，参考 `series_options.LabelOpts`
    label_opts: Union[opts.LabelOpts, dict] = opts.LabelOpts(),

    # 标记点配置项，参考 `series_options.MarkPointOpts`
    markpoint_opts: Union[opts.MarkPointOpts, dict, None] = None,

    # 标记线配置项，参考 `series_options.MarkLineOpts`
    markline_opts: Union[opts.MarkLineOpts, dict, None] = None,

    # 提示框组件配置项，参考 `series_options.TooltipOpts`
    tooltip_opts: Union[opts.TooltipOpts, dict, None] = None,

    # √ 图元样式配置项，参考 `series_options.ItemStyleOpts`
    itemstyle_opts: Union[opts.ItemStyleOpts, dict, None] = None,

    # 可以定义 data 的哪个维度被编码成什么。
    encode: types.Union[types.JSFunc, dict, None] = None,
)