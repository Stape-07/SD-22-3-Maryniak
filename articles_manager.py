import sqlite3

conn = sqlite3.connect('articles.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Articles (
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    content TEXT NOT NULL,
    author TEXT UNIQUE
)
''')

def add_article(title, content, author):
    try:
        cursor.execute('''
            INSERT INTO Articles (title, content, author)
            VALUES (?, ?, ?)
        ''', (title, content, author))
        conn.commit()
        print("✅ Статтю додано.")
    except sqlite3.IntegrityError:
        print("❌ Помилка: автор має бути унікальним!")

def delete_article(article_id):
    cursor.execute('DELETE FROM Articles WHERE id = ?', (article_id,))
    conn.commit()
    print("🗑️ Статтю видалено.")

def view_articles():
    cursor.execute('SELECT * FROM Articles')
    articles = cursor.fetchall()
    for article in articles:
        print(f"ID: {article[0]}, Назва: {article[1]}, Автор: {article[3]}")
        print(f"Зміст: {article[2]}")
        print('-' * 40)

def close_connection():
    conn.close()
