#!/usr/bin/python3
import psycopg2
conn = psycopg2.connect(database = "имя БД", user = "имя пользователя", password = "пароль", host = "127.0.0.1", port = "5432")
print ("Opened database successfully")

cur = conn.cursor()
cur.execute('DROP TABLE IF EXISTS CLIENTS')
conn.commit()
cur.execute('CREATE TABLE  CLIENTS (ID TEXT PRIMARY KEY NOT NULL, NAME TEXT NOT NULL, POSITION INT NOT NULL, REG_DATE TIMESTAMP NOT NULL);')
print ("Table created successfully")

conn.commit()
conn.close()
