#!/usr/bin/python3
import uuid
import psycopg2
conn = psycopg2.connect(database="_______", user="_________", password="___________", host="127.0.0.1", port="5432")
print("Opened database successfully")

cur = conn.cursor()
def quiz_result (qid, answer):
    postgres_select_query = """SELECT answer FROM questions WHERE id = %s"""
    cur.execute(postgres_select_query, (qid,))
    row = cur.fetchone()
    result = row[0]
    print ("Правильный ответ: ", result, " Ваш ответ: ", answer)
    cur.close()
    if str(result) == answer: return True
    return False

def quiz_question (qid):
    postgres_select_query = """SELECT question FROM questions WHERE id = %s"""
    cur.execute(postgres_select_query, (qid,))
    row = cur.fetchone()
    result = row[0]
    return result

def say_next (pos):
    postgres_select_query = """SELECT message FROM talks WHERE id = %s"""
    cur.execute(postgres_select_query, (pos,))
    row = cur.fetchone()
    result = row[0]
    return result

#print (quiz_question("885fc913-a151-40af-b56a-2d6249a82fb2"))
#print (quiz_result ("885fc913-a151-40af-b56a-2d6249a82fb2", "1"))
pos = 1
while pos < 6:
  print (say_next(pos))
  pos += 1

cur.close()

