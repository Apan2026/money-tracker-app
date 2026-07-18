# database.py
import sqlite3
import os
from datetime import datetime

DB_NAME = 'money_tracker.db'

def get_connection():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_connection()
    cursor = conn.cursor()
    
    # Users table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    ''')
    
    # Transactions table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS transactions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL,
        type TEXT NOT NULL,
        amount REAL NOT NULL,
        category TEXT,
        date TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY(username) REFERENCES users(username)
    )
    ''')
    
    conn.commit()
    conn.close()

def register_user(username, password):
    if not username or not password:
        return False, "Fill all fields"
    
    conn = get_connection()
    cursor = conn.cursor()
    
    try:
        cursor.execute('''
        INSERT INTO users (username, password)
        VALUES (?, ?)
        ''', (username, password))
        
        conn.commit()
        conn.close()
        return True, "Registration successful"
    except sqlite3.IntegrityError:
        conn.close()
        return False, "Username already exists"
    except Exception as e:
        conn.close()
        return False, str(e)

def login_user(username, password):
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute('''
    SELECT username FROM users
    WHERE username=? AND password=?
    ''', (username, password))
    
    user = cursor.fetchone()
    conn.close()
    
    if user:
        return True, user[0]
    else:
        return False, None

def add_transaction(username, t_type, amount, category, date):
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute('''
    INSERT INTO transactions (username, type, amount, category, date)
    VALUES (?, ?, ?, ?, ?)
    ''', (username, t_type, amount, category, date))
    
    conn.commit()
    conn.close()

def get_report(username):
    conn = get_connection()
    cursor = conn.cursor()
    
    # Total income
    cursor.execute('''
    SELECT SUM(amount) FROM transactions
    WHERE username=? AND type='income'
    ''', (username,))
    
    income = cursor.fetchone()[0] or 0
    
    # Total expense
    cursor.execute('''
    SELECT SUM(amount) FROM transactions
    WHERE username=? AND type='expense'
    ''', (username,))
    
    expense = cursor.fetchone()[0] or 0
    
    conn.close()
    
    return {
        'income': income,
        'expense': expense,
        'balance': income - expense
    }

def get_transactions(username):
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute('''
    SELECT type, amount, category, date
    FROM transactions
    WHERE username=?
    ORDER BY id DESC
    ''', (username,))
    
    data = cursor.fetchall()
    conn.close()
    
    return data
