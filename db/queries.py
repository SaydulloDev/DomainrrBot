import sqlite3

# Statistics user
STATISTICS_USER = 'SELECT COUNT(*) FROM users'
# update language
UPDATE_LANGUAGE = 'UPDATE users SET lang = ? WHERE user_id = ?'
# Select all Users ID and Send Message
ALL_USERS_ID = 'SELECT user_id FROM users'


# -------------------------------- func --------------------------------
def get_lang_user(user_id):
    with sqlite3.connect('db/db.sqlite3') as connection:
        cursor = connection.cursor()
        cursor.execute('SELECT lang FROM users WHERE user_id = ?', (user_id,))
        result = cursor.fetchall()
        print(result)
        return result[0][0]


def check_user_registry(user_id):
    with sqlite3.connect('db/db.sqlite3') as connection:
        cursor = connection.cursor()
        cursor.execute('SELECT user_id FROM users WHERE user_id = ?', (user_id,))
        result = cursor.fetchall()
        print(result)
        if result:
            return True
        else:
            return False


def registry_user(user_id, first_name, lang, username=None):
    with sqlite3.connect('db/db.sqlite3') as connection:
        cursor = connection.cursor()
        cursor.execute('INSERT INTO users (user_id, first_name, username, lang) VALUES (?, ?,?, ?)',
                       (user_id, first_name, username, lang))
        return True


def update_language(lang, user_id):
    with sqlite3.connect('db/db.sqlite3') as connection:
        cursor = connection.cursor()
        cursor.execute('UPDATE users SET lang = ? WHERE user_id = ?', (lang, user_id))
        result = cursor.fetchall()
        if result is not None:
            return True
        return False


def stat():
    with sqlite3.connect('db/db.sqlite3') as connection:
        cursor = connection.cursor()
        cursor.execute('SELECT COUNT(*) FROM users')
        result = cursor.fetchall()
        return result[0][0]
