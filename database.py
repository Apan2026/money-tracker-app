# database.py

import sqlite3

DB_NAME = "money_tracker.db"


def connect():
    return sqlite3.connect(DB_NAME)


def create_tables():
    conn = connect()
    cursor = conn.cursor()

    # User table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL
    )
    """)

    # Transaction table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS transactions(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL,
        type TEXT NOT NULL,
        amount REAL NOT NULL,
        category TEXT,
        date TEXT
    )
    """)

    conn.commit()
    conn.close()


def add_transaction(username, t_type, amount, category, date):

    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO transactions
    (username, type, amount, category, date)
    VALUES (?, ?, ?, ?, ?)
    """,
    (
        username,
        t_type,
        amount,
        category,
        date
    ))

    conn.commit()
    conn.close()