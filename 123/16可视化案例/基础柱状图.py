from pyecharts.charts import *
from pyecharts.options import *
bar = Bar()  # 构建基础柱状图
bar.add_xaxis(["中国", "美国", "英国"])
bar.add_yaxis("GDP", [30, 20, 10], label_opts=LabelOpts(position="right"))  # 后面段是让数值表情放在图形柱子的最右边
bar.reversal_axis()  # 反转xy轴

timeline.add_schema(
    play_interval
)

bar.render("基础柱状图.html")
