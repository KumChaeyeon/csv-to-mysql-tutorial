import pandas as pd
import pymysql

data = pd.read_csv("orders.csv")

conn = pymysql.connect(
    host="localhost",
    user="root",
    password="1234",
    database="tutorial_db"
)

cursor = conn.cursor()

for _, row in data.iterrows():
    sql = "INSERT INTO orders (product, price) VALUES (%s, %s)"
    cursor.execute(sql, (row["product"], row["price"]))

conn.commit()
conn.close()

print("데이터 저장 완료")