from pyecharts.options import TitleOpts
from pyecharts.charts import Map
from pyecharts.options import VisualMapOpts
# 准备地图对象
map = Map()
# 准备数据
data = [("北京", 9), ("上海", 99), ("湖南", 199), ("台湾", 299), ("广东", 399)]
map.add("测试地图", data, "china")


map.set_global_opts(
    title_opts=TitleOpts(title="全国各地确诊人数", pos_left="center", pos_bottom="1%"),
    visualmap_opts=VisualMapOpts(
        is_show=True,
        is_piecewise=True,
        pieces=[
            {"man": 1, "max": 9, "label": "1-9", "color": "#FFA500"},
            {"man": 10, "max": 99, "label": "10-99", "color": "#FF0000"},
            {"man": 100, "max": 500, "label": "100-500", "color": "#B22222"},

        ]
    )
)


# 绘图
map.render()
