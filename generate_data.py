#!/usr/bin/python3
# coding=utf-8

import asyncio
from random import randint

# import aiomysql
import aiosqlite3
from faker import Faker
from pymysql import connect


def tmp():
    idn = "a123"
    psd = "q111"
    userid = input("please input id:")

    if userid == idn:
        passed = input("""please input password:""")
        if passed == psd:
            print("login success!")
        else:
            print("password error! please reinput")
    else:
        print("ID error! please input")

    from django.contrib.auth import get_user_model

    User = get_user_model()
    User.objects.create_superuser('admin', "admin@base.io", "12345678")


fake = Faker(locale='zh_CN')
# zh_CN,zh_TW,en_US


sex = {1: "female", 0: "male"}


def get_data():
    ...


def create_table(host, passwd, user="root", callback=None):
    student_table = """-- stu.student definition

CREATE TABLE `student` (
  `sno` varchar(20) PRIMARY KEY NOT NULL,
  `sname` varchar(20) NOT NULL,
  `ssex` varchar(20) NOT NULL,
  `sbrithday` datetime DEFAULT NULL,
  `class` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;"""

    teacher_table = """-- stu.teacher definition

CREATE TABLE `teacher` (
  `tno` varchar(20) PRIMARY KEY NOT NULL,
  `tname` varchar(20) NOT NULL,
  `tsex` varchar(20) NOT NULL,
  `tbrithday` datetime DEFAULT NULL,
  `prof` varchar(20) DEFAULT NULL,
  `depart` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;"""

    course_table = """-- stu.course definition

CREATE TABLE `course` (
  `cno` varchar(20) PRIMARY KEY NOT NULL,
  `cname` varchar(20) NOT NULL,
  `tno` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;"""

    score_table = """-- stu.score definition

CREATE TABLE `score` (
  `sno` varchar(20) NOT NULL,
  `cno` varchar(20) NOT NULL,
  `degree` decimal(4,1) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;"""

    # return "\n".join([student_table, teacher_table, course_table,
    # score_table])
    sql = student_table + "\n" + teacher_table + \
          "\n" + course_table + "\n" + score_table
    print(sql)
    _conn = connect(
        host=host,
        port=3306,
        user=user,
        password=passwd,
        db='test'
    )
    _cursor = _conn.cursor()
    _cursor.execute(sql)
    _conn.commit()
    _cursor.close()
    _conn.close()


def insert_data_polls_question():
    data = []
    for i in range(1, 31):
        sql = f"""INSERT INTO polls_question (question_text,pub_date)
            VALUES ("{fake.name()}",
            "{fake.date('%Y-%m-%d %H:%M:%S', end_datetime=None)}"); """
        data.append(sql)
    return data


def insert_data_polls_choice():
    data = []
    for i in range(1, 31):
        sql = f"""INSERT INTO polls_choice (choice_text,votes,question_id)
        VALUES ('{fake.name()}',{randint(0, 100)},{i % 3 + 12}                );"""
        data.append(sql)
    return data


async def execute(db, callback=None):
    print("running db is", db)

    conn = await aiosqlite3.connect(database=db)

    cur = await conn.cursor()

    for sql_line in callback():
        await cur.execute(sql_line)
    # await cur.execute("select * from student;")

    # result = await cur.fetchall()
    # print(result)

    await conn.commit()

    await cur.close()
    conn.close()
    print("run end db ", db)


def main():
    # asyncio.run(execute('localhost', "123456"))

    task_list = [
        execute("db.sqlite3", callback=insert_data_polls_question),
        # execute("db.sqlite3", callback=insert_data_polls_choice),
    ]

    # loop = asyncio.new_event_loop()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.gather(*task_list))
    # asyncio.run(asyncio.wait(task_list))


if __name__ == '__main__':
    # create_table('localhost', "1234", )
    main()
