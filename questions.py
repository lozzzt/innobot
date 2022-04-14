#!/usr/bin/python3
import uuid
import psycopg2
import psycopg2.extras
psycopg2.extras.register_uuid()

id = str(uuid.uuid4())
question1 = "К какому типу относится сотрудник который и способен и настроен выполнить задачу?"
answer1 = "4"
conn = psycopg2.connect(database="_______", user="________", password="______", host="127.0.0.1", port="5432")
print("Opened database successfully")

cur = conn.cursor()

postgres_insert_query = """INSERT INTO questions (ID, QUESTION, ANSWER) VALUES (%s,%s,%s) ON CONFLICT DO NOTHING"""
record_to_insert = (id, question1, answer1)
cur.execute(postgres_insert_query, record_to_insert)

conn.commit()
