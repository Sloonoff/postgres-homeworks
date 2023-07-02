"""Скрипт для заполнения данными таблиц в БД Postgres."""

import psycopg2
import csv

if __name__ == '__main__':

    with psycopg2.connect(host='localhost', database='north', user='postgres', password='nba2k9') as connection:

        with connection.cursor() as cur:
            emp_file = list(csv.reader(open('north_data/employees_data.csv', encoding='utf-8')))
            cust_file = list(csv.reader(open('north_data/customers_data.csv', encoding='utf-8')))
            ord_file = list(csv.reader(open('north_data/orders_data.csv', encoding='utf-8')))
            del emp_file[0]
            del cust_file[0]
            del ord_file[0]
            for data in emp_file:
                cur.execute('INSERT INTO employees VALUES (%s, %s, %s, %s, %s, %s)', tuple(data))
            for data in cust_file:
                cur.execute('INSERT INTO customers VALUES (%s, %s, %s)', tuple(data))
            for data in ord_file:
                cur.execute('INSERT INTO orders VALUES (%s, %s, %s, %s, %s)', tuple(data))

    connection.close()
