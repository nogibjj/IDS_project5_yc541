import sqlite3
import os


def connectDB(database_name):
    conn = sqlite3.connect(database_name)
    cursor = conn.cursor()
    return conn, cursor


def createDB(cursor):
    cursor.execute(
        """
    CREATE TABLE IF NOT EXISTS jobs (
        job_id INTEGER PRIMARY KEY,
        company_name TEXT,
        job_name TEXT,
        posted_date DATE,
        job_type TEXT,
        position_count INTEGER
    )
    """
    )


def insertDB(
    cursor, job_id, company_name, job_name, posted_date, job_type, position_count
):
    cursor.execute(
        "INSERT INTO jobs (job_id, company_name, job_name, posted_date, job_type, position_count) VALUES (?, ?, ?, ?, ?, ?)",
        (job_id, company_name, job_name, posted_date, job_type, position_count),
    )


def readDB(cursor):
    cursor.execute("SELECT * FROM jobs")
    return cursor.fetchall()


def updateDB(cursor, job_id, new_posted_date):
    cursor.execute(
        "UPDATE jobs SET posted_date = ? WHERE job_id = ?", (new_posted_date, job_id)
    )


def deleteDB(cursor, job_id):
    cursor.execute("DELETE FROM jobs WHERE job_id = ?", (job_id,))


def query1(cursor):
    cursor.execute("SELECT COUNT(*) FROM jobs")
    count = cursor.fetchone()[0]
    return count


def query2(cursor):
    cursor.execute("SELECT * FROM jobs WHERE posted_date < '2022-01-01'")
    older_jobs = cursor.fetchall()
    return older_jobs


def main():
    database_name = "jobsDB.db"
    if os.path.exists(database_name):
        os.remove(database_name)

    conn, cursor = connectDB(database_name)

    # C
    createDB(cursor)
    insertDB(
        cursor, 55176, "Amazon", "Backend Developer", "2023-09-28", "experienced", 500
    )
    insertDB(
        cursor,
        55176,
        "Amazon",
        "Associate Software Develope",
        "2023-09-27",
        "new grads",
        400,
    )
    insertDB(
        cursor, 87356, "LinkedIn", "Fullstack Developer", "2023-09-27", "new grads", 300
    )
    insertDB(cursor, 99345, "Google", "Technolog Analyst", "2023-09-26", "intern", 200)
    insertDB(
        cursor, 70001, "Apple", "Software Engineer", "2023-09-25", "new grads", 100
    )
    insertDB(
        cursor,
        80002,
        "Oracle",
        "Associate Software Developer",
        "2023-09-24",
        "experienced",
        250,
    )
    insertDB(
        cursor,
        90102,
        "Veeva System",
        "Associate Software Developer",
        "2023-09-24",
        "new grads",
        350,
    )

    # R
    print(readDB(cursor))

    # U
    updateDB(cursor, 99345, "2023-09-29")
    print(readDB(cursor))

    # D
    deleteDB(cursor, 10001)
    print(readDB(cursor))

    # Queries
    query1(cursor)
    query2(cursor)

    conn.commit()
    conn.close()


if __name__ == "__main__":
    main()
