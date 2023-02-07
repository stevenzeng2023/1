from pyecharts.charts import *
from pyecharts.options import *
import json
f = open("F:/py/16可视化案例/疫情.txt", "r", encoding="UTF-8")
province_data = f.read()
data_dict = json.loads(province_data)
city_data_list = data_dict["areaTree"][0]["children"][7]["children"]
data = []
for i in range(len(city_data_list)):
    data.append([city_data_list[i]['name'] + "市", city_data_list[i]['total']['confirm']])
# print(data)
map = Map()
map.add("广东疫情地图", data, "广东")
map.set_global_opts(
    title_opts=TitleOpts(title="广东各市确诊人数", pos_left="center", pos_bottom="1%"),
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
map.render("广东疫情地图.html")
