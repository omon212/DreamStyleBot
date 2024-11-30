import sqlite3

connect = sqlite3.connect('./user_data.db')
cursor = connect.cursor()

cursor.execute(
    """CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    user_id INTEGER,
    full_name TEXT,
    username TEXT,
    phone_number TEXT,
    language TEXT)
    """)


