from pymysql import Connection

# 获取Mysql数据库的连接对象
conn = Connection(
    host="localhost",  # 主机名，表示本机
    port=3306,
    user="root",
    password="123456"
)
# 获取游标对象
cursor = conn.cursor()
# # 选择数据库
# conn.select_db("test")
# cursor.execute("create table test_pymysql(id int);")
# 获取查询结果
conn.select_db("world")
cursor.execute("select * from student")
results = cursor.fetchall()
for r in results:
    print(r)

conn.close()
