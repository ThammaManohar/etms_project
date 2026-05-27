import sqlite3


def get_connection():
    conn = sqlite3.connect("etms.db")
    return conn


def create_tables():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS employees (
        emp_id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        email TEXT NOT NULL
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS tasks (
        task_id INTEGER PRIMARY KEY,
        title TEXT NOT NULL,
        assigned_to INTEGER,
        status TEXT,
        FOREIGN KEY (assigned_to) REFERENCES employees(emp_id)
    )
    """)

    conn.commit()
    conn.close()