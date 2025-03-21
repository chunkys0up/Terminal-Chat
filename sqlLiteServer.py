import sqlite3

# Database connection
conn = sqlite3.connect("terminal_conversation.db")
cur = conn.cursor()

#data will keep on duplicating unless you clear the database each time you run this sqliteserver
cur.execute("DELETE FROM terminal_conversation")
conn.commit()

# Create table if it doesn't exist
cur.execute("CREATE TABLE IF NOT EXISTS terminal_conversation (sender, message)")


def addQuery(name: str, msg: str):
    data = [name, msg]
    cur.execute("INSERT INTO terminal_conversation VALUES(?, ?)", data)
    conn.commit()


def clientSideHistory():
    for row in cur.execute("SELECT * FROM terminal_conversation"):
        print(row)


def printMessages():
    res = cur.execute("SELECT * FROM terminal_conversation")
    print(res.fetchall())


addQuery("Andrew", "You free sat?")
addQuery("John", "No")
addQuery("Andrew", "ok")

clientSideHistory()

conn.close()
