from jobs_database import (
    connectDB,
    createDB,
    insertDB,
    readDB,
    updateDB,
    deleteDB,
    query1,
    query2,
)
import os

DATABASE_NAME = "jobs_database.db"



def test_create_and_insert():
    conn, cursor = connectDB(DATABASE_NAME)
    createDB(cursor)
    insertDB(
        cursor, 55176, "Amazon", "Software Engineer", "2022-09-30", "New Grads", 500
    )

    cursor.execute("SELECT * FROM jobs WHERE job_id=?", (55176,))
    result = cursor.fetchone()
    assert result == (
        55176,
        "Amazon",
        "Software Engineer",
        "2022-09-30",
        "New Grads",
        500,
    )


def test_read():
    conn, cursor = connectDB(DATABASE_NAME)
    createDB(cursor)
    insertDB(
        cursor, 55176, "Amazon", "Software Engineer", "2022-09-30", "New Grads", 500
    )
    insertDB(
        cursor, 87356, "Google", "Backend Developer", "2022-09-20", "Experienced", 300
    )

    info = readDB(cursor)
    assert len(info) == 2


def test_update():
    conn, cursor = connectDB(DATABASE_NAME)
    createDB(cursor)
    insertDB(
        cursor, 55177, "Amazon", "Software Engineer", "2022-09-30", "New Grads", 500  # 注意这里，job_id 改为 55177
    )
    updateDB(
        cursor, 55177, "2022-10-01"
    )
    cursor.execute("SELECT * FROM jobs WHERE job_id=?", (55177,))
    result = cursor.fetchone()
    assert result == (
        55177,
        "Amazon",
        "Software Engineer",
        "2022-10-01",
        "New Grads",
        500,
    )



def test_delete():
    conn, cursor = connectDB(DATABASE_NAME)
    createDB(cursor)
    insertDB(
        cursor, 55176, "Amazon", "Software Engineer", "2022-09-30", "New Grads", 500
    )
    insertDB(
        cursor, 87356, "Google", "Backend Developer", "2022-09-20", "Experienced", 300
    )

    deleteDB(cursor, 55176)
    info = readDB(cursor)
    assert len(info) == 1


def test_query1():
    if os.path.exists("jobsDB.db"):
        os.remove("jobsDB.db")
    conn, cursor = connectDB(DATABASE_NAME)
    # 使用insertDB来插入测试数据
    insertDB(
        cursor, 55176, "Amazon", "Fullstack Developer", "2022-09-30", "New Grads", 550
    )
    result = query1(cursor)
    assert result == 1  # 我们刚刚插入了一个工作岗位


def test_query2():
    if os.path.exists("jobsDB.db"):
        os.remove("jobsDB.db")
    conn, cursor = connectDB(DATABASE_NAME)
    insertDB(
        cursor, 55176, "Amazon", "Fullstack Developer", "2021-09-29", "New Grads", 550
    )
    results = query2(cursor)
    for job in results:
        assert job[3] < "2022-01-01"  # 确保工作发布日期在2022年1月1日之前
