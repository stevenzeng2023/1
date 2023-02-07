from pyecharts.charts import Bar, Timeline
from pyecharts.options import *
from pyecharts.globals import ThemeType
# 读取数据
f = open("F:/py/16可视化案例/1960-2019全球GDP数据.csv", "r", encoding="GB2312")
data_lines = f.readlines()
f.close()
# 删除第一条数据
data_lines.pop(0)
# 将数据变成字典 年份为key
data_dict = {}
for line in data_lines:
    year = int(line.split(",")[0])  # 提取年份
    country = line.split(",")[1]  # 提取国家
    gdp = float(line.split(",")[2])  # 提取GDP数据
    try:
        data_dict[year].append([country, gdp])
    except KeyError:
        data_dict[year] = []
        data_dict[year].append([country, gdp])
# print(data_dict)
timeline = Timeline({"theme": ThemeType.DARK})
# 排序年份
sorted_year_list = sorted(data_dict.keys())
# print(sorted_year_list)
for year in sorted_year_list:
    data_dict[year].sort(key=lambda element: element[1], reverse=True)
    year_data = data_dict[year][0:8]
    x_data = []
    y_data = []
    for country_gdp in year_data:
        x_data.append(country_gdp[0])
        y_data.append(country_gdp[1] / 100000000)

    bar = Bar()
    x_data.reverse()
    y_data.reverse()
    bar.add_xaxis(x_data)
    bar.add_yaxis("GDP(亿)", y_data, label_opts=LabelOpts(position="right"))
    # 反转xy轴
    bar.reversal_axis()
    bar.set_global_opts(
        title_opts=TitleOpts(title=f"{year}年全球GDP数量")
    )

    timeline.add(bar, str(year))

# 设置自动播放
timeline.add_schema(
    play_interval=100,
    is_timeline_show=True,
    is_auto_play=True,
    is_loop_play=False
)

# 绘图
timeline.render("1960-2019全球GDP前8国家.html")


