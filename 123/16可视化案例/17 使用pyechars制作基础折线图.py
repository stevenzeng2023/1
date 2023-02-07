from pyecharts.charts import Line
from pyecharts.options import TitleOpts, LegendOpts, ToolboxOpts, VisualMapOpts
line = Line() # 创建一个折线图对象
line.add_xaxis(["中国", "美国", "英国"])  # x轴数据
line.add_yaxis("GDP", [30, 20, 10])  # y轴数据
# 设置全局配置 set_global_opts来设置
line.set_global_opts(
    title_opts=TitleOpts(title="GDP展示", pos_left="center", pos_bottom="1%"),
    legend_opts=LegendOpts(is_show=True),
    toolbox_opts=ToolboxOpts(is_show=True),
    visualmap_opts=VisualMapOpts(is_show=True)

)



# 通过render方法，将代码生成图形
line.render()
