#!/usr/bin/python3
import psycopg2
import yaml

with open("config.yaml", "r") as ymlfile:
    config = yaml.safe_load(ymlfile)

db = config['DB']
connect = psycopg2.connect(database=db['NAME'], user=db['USER'], password=db['PASSWORD'], host=db['HOST'], port=db['PORT'])
print ("Opened database successfully")

cur = connect.cursor()
cur.execute('DROP TABLE IF EXISTS CLIENTS')
connect.commit()
cur.execute('CREATE TABLE CLIENTS (ID SERIAL PRIMARY KEY, NAME TEXT NOT NULL, REG_DATE TIMESTAMP NOT NULL);')
print ("Table created successfully")

connect.commit()
connect.close()
