import sqlite3


def get_connection():
    """
    Create and return a database connection
    """
    return sqlite3.connect("etms.db")


def create_tables():
    """
    Create employees and tasks tables if they don't exist
    """
    conn = get_connection()
    cursor = conn.cursor()

    # Create employees table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS employees (
        emp_id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        email TEXT NOT NULL
    )
    """)

    # Create tasks table
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


def reset_tables():
    """
    Delete all data from tables (for fresh testing)
    """
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM tasks")
    cursor.execute("DELETE FROM employees")

    conn.commit()
    conn.close()