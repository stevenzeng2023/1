# json 编程语言中转
# 准备列表，列表内每一个元素都是字典，将其转换为json
import json

data = [{"name": "张三", "age": 15}, {"name": "李四", "age": 14}, {"name": "吴五", "age": 18}]
json_str = json.dumps(data, ensure_ascii=False) # ensure_ascii=False是用于将字符转为中文显示
# 准备字典，将字典转换成JSON
d = {"name": "周轮", "addr": "太白山"}
json.dumps(d, ensure_ascii=False)


# 将JSON字符串转换为Python数据类型[{k: v, k: v}, {k: v, k: v}]
s = '[{"name": "张三", "age": 15}, {"name": "李四", "age": 14}, {"name": "吴五", "age": 18}]'
l = json.loads(s)

# 将JSON字符串转换为Python数据类型{k: v, k: v}
s = '{"name": "周轮", "addr": "太白山"}'
d = json.loads(s)
