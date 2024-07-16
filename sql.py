import sqlite3
import datetime

connection = sqlite3.connect("tutorial-db")
cur = connection.cursor()
cur.execute("CREATE TABLE chatHistory(sessionToken, role, message, timeStamp)")
