"""
全国疫情地图
"""
import json
from pyecharts.charts import Map
from pyecharts.options import *


f = open("F:/py/16可视化案例/疫情.txt", "r", encoding="UTF-8")
f_data = f.read()
f.close()
f_dict = json.loads(f_data)
province_data_list = f_dict["areaTree"][0]["children"]
data = []
for province_data in province_data_list:
    f_name = province_data["name"]
    f_confirm = province_data["total"]["confirm"]
    data.append((f_name, f_confirm))
# print(data)
map = Map()
map.add("全国疫情地图", data, "china")
map.set_global_opts(
    title_opts=TitleOpts(title="全国各地确诊人数", pos_left="center", pos_bottom="1%"),
    visualmap_opts=VisualMapOpts(
        is_show=True,
        is_piecewise=True,
        pieces=[
            {"min": 1, "max": 9, "label": "1-9", "color": "#B0E2FF"},
            {"min": 10, "max": 99, "label": "10-99", "color": "#FF0000"},
            {"min": 100, "max": 499, "label": "100-499", "color": "#B22222"},
            {"min": 500, "max": 999, "label": "100-999", "color": "#B22222"},
            {"min": 1000, "max": 9999, "label": "1000-9999", "color": "#B22222"},
            {"min": 10000, "max": 99999, "label": "10000-99999", "color": "#B22222"},
            {"min": 10000, "label": "100000+", "color": "#B22222"},
           ]
    )
)

map.render("全国疫情地图1.html")
