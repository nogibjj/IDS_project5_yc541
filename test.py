from jobs_database import connectDB, createDB, insertDB, readDB, updateDB, deleteDB, complexQuery1, complexQuery2
import os

DATABASE_NAME = "jobs_database.db"

def setup_function():
    if os.path.exists(DATABASE_NAME):
        os.remove(DATABASE_NAME)

def test_create_and_insert():
    conn, cursor = connectDB(DATABASE_NAME)
    createDB(cursor)
    insertDB(cursor, 55176, "Amazon", "Software Engineer", "2022-09-30", "New Grads", 500)
    
    cursor.execute("SELECT * FROM jobs WHERE job_id=?", (55176,))
    result = cursor.fetchone()
    assert result == (55176, "Amazon", "Software Engineer", "2022-09-30", "New Grads", 500)

def test_read():
    conn, cursor = connectDB(DATABASE_NAME)
    createDB(cursor)
    insertDB(cursor, 55176, "Amazon", "Software Engineer", "2022-09-30", "New Grads", 500)
    insertDB(cursor, 87356, "Google", "Backend Developer", "2022-09-20", "Experienced", 300)
    
    info = readDB(cursor)
    assert len(info) == 2

def test_update():
    conn, cursor = connectDB(DATABASE_NAME)
    createDB(cursor)
    insertDB(cursor, 55176, "Amazon", "Software Engineer", "2022-09-30", "New Grads", 500)
    
    updateDB(cursor, 55176, "Amazon", "Fullstack Developer", "2022-09-30", "New Grads", 550)
    cursor.execute("SELECT * FROM jobs WHERE job_id=?", (55176,))
    result = cursor.fetchone()
    assert result == (55176, "Amazon", "Fullstack Developer", "2022-09-30", "New Grads", 550)

def test_delete():
    conn, cursor = connectDB(DATABASE_NAME)
    createDB(cursor)
    insertDB(cursor, 55176, "Amazon", "Software Engineer", "2022-09-30", "New Grads", 500)
    insertDB(cursor, 87356, "Google", "Backend Developer", "2022-09-20", "Experienced", 300)
    
    deleteDB(cursor, 55176)
    info = readDB(cursor)
    assert len(info) == 1

def test_complex_query1():
    conn, cursor = connectDB(DATABASE_NAME)
    createDB(cursor)
    insertDB(cursor, 55176, "Amazon", "Software Engineer", "2022-09-30", "New Grads", 500)
    insertDB(cursor, 87356, "Google", "Backend Developer", "2022-09-20", "Experienced", 300)
    
    result = complexQuery1(cursor)
    assert len(result) == 1  # Modify based on the expected length of result after running complexQuery1

def test_complex_query2():
    conn, cursor = connectDB(DATABASE_NAME)
    createDB(cursor)
    insertDB(cursor, 55176, "Amazon", "Software Engineer", "2022-09-30", "New Grads", 500)
    insertDB(cursor, 87356, "Google", "Backend Developer", "2022-09-20", "Experienced", 300)
    
    result = complexQuery2(cursor)
    assert len(result) == 2  # Modify based on the expected length of result after running complexQuery2
