from file_define import *
from data_define import *
from pyecharts.charts import Bar
from pyecharts.options import *
from pyecharts.globals import ThemeType

txt_file_reader = TxtFileReader("F:/py/练习-数据分析案例/2011年1月销售数据.txt")
json_file_reader = JsonFileReader("F:/py/练习-数据分析案例/2011年2月销售数据JSON.txt")

jan_data: list[Record] = txt_file_reader.read_data()
feb_data: list[Record] = json_file_reader.read_data()

all_data: list[Record] = jan_data + feb_data

data_dict = {}
for record in all_data:
    if record.date in data_dict.keys():
        data_dict[record.date] += record.money
    else:
        data_dict[record.date] = record.money


bar = Bar(init_opts=InitOpts(ThemeType.LIGHT))

bar.add_xaxis(list(data_dict.keys()))
bar.add_yaxis("销售额", list(data_dict.values()), label_opts=LabelOpts(is_show=False))
bar.set_global_opts(
    title_opts=TitleOpts(title="每日销售额")
)
bar.render("每日销售额柱状图.html")
