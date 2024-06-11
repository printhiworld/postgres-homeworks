import psycopg2
import csv

conn = psycopg2.connect(
    host='localhost',
    database='north',
    user='postgres',
    password='123456'
)

cur = conn.cursor()

with open('north_data/employees_data.csv', 'r', newline='') as csvfile:
    rows = csv.reader(csvfile)
    next(rows)
    for row in rows:
        cur.execute("insert into  employees values(%s, %s, %s, %s, %s, %s)", (row[0], row[1], row[2], row[3], row[4], row[5]))

with open('north_data/customers_data.csv', 'r', newline='') as csvfile:
    rows = csv.reader(csvfile)
    next(rows)
    for row in rows:
        cur.execute("insert into  customers values(%s, %s, %s)", (row[0], row[1], row[2]))

with open('north_data/orders_data.csv', 'r', newline='') as csvfile:
    rows = csv.reader(csvfile)
    next(rows)
    for row in rows:
        cur.execute("insert into  orders values(%s, %s, %s, %s, %s)", (row[0], row[1], row[2], row[3], row[4]))

conn.commit()
cur.close()
conn.close()