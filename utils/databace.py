import sqlite3

connect = sqlite3.connect('./user_data.db')
cursor = connect.cursor()

cursor.execute(
    """CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    user_id INTEGER NULL,
    full_name TEXT NULL,
    username TEXT NULL,
    phone_number TEXT NULL,
    language TEXT NULL)
    """)


async def check_user(user_id, ):
    user = cursor.execute("SELECT * FROM users WHERE user_id = ?", (user_id,)).fetchone()
    if user:
        return user
    else:
        return False


async def save_language(user_id, language):
    cursor.execute("SELECT * FROM users WHERE user_id = ?", (user_id,))
    user_exists = cursor.fetchone()

    if user_exists:
        cursor.execute("UPDATE users SET language = ? WHERE user_id = ?", (language, user_id))
    else:
        cursor.execute("INSERT INTO users (user_id, language) VALUES (?, ?)", (user_id, language))
    connect.commit()


async def save_user_data(user_id, full_name, username, phone_number):
    cursor.execute("SELECT * FROM users WHERE user_id = ?", (user_id,))
    user_exists = cursor.fetchone()

    if user_exists:
        cursor.execute("UPDATE users SET full_name = ?, username = ?, phone_number = ? WHERE user_id = ?",
                       (full_name, username, phone_number, user_id))
    else:
        cursor.execute("INSERT INTO users (user_id, full_name, username, phone_number) VALUES (?, ?, ?, ?)",
                       (user_id, full_name, username, phone_number))
    connect.commit()
