import sqlite3

# Database connection
conn = sqlite3.connect("conversation.db")
cur = conn.cursor()

# Clear existing data before inserting new data
cur.execute("DELETE FROM conversation")
conn.commit()

# Create table if it doesn't exist
cur.execute("""
    CREATE TABLE IF NOT EXISTS conversation (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        sender TEXT,
        message TEXT
    )
""")


def addQuery(name: str, msg: str):
    cur.execute(f"""INSERT INTO conversation VALUE
                ({name}, {msg})
                """)
    conn.commit()


def printMessages():
    res = cur.execute("SELECT * FROM conversation")
    print(res.fetchall())


addQuery("Andrew", "How are you?")
addQuery("John", "Good")


conn.close()
