from file_define import TxtFileReader, JsonFileReader
from data_define import Record
from pymysql import Connection

txt_file_reader = TxtFileReader("F:/py/练习-数据分析案例/2011年1月销售数据.txt")
json_file_reader = JsonFileReader("F:/PY/练习-数据分析案例/2011年2月销售数据JSON.txt")

jan_data: list[Record] = txt_file_reader.read_data()
feb_data: list[Record] = json_file_reader.read_data()
all_data: list[Record] = jan_data + feb_data

conn = Connection(
    host="localhost",
    port=3306,
    user="root",
    password="123456",
    autocommit=True

)

cursor = conn.cursor()
cursor.execute("create database py_sql charset utf8")
conn.select_db("py_sql")
cursor.execute(
    "create table orders(order_date DATE, order_id varchar(255), money int, province varchar(10));"
    )
for record in all_data:
    sql = f"insert into orders(order_date, order_id, money, province) " \
          f"values('{record.date}','{record.order_id}', {record.money}, '{record.province}')"
    cursor.execute(sql)

conn.close()
