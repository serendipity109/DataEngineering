import mysql.connector
from mysql.connector import Error

def write_read():
    conn = mysql.connector.connect(
        host="127.0.0.1",
        port=5600,
        user="root",
        password="root"
    )
    cursor = conn.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS demo;")
    cursor.execute("USE demo;")
    cursor.execute("CREATE TABLE IF NOT EXISTS logs (id INT AUTO_INCREMENT PRIMARY KEY, msg VARCHAR(100));")
    cursor.execute("INSERT INTO logs (msg) VALUES ('Test message');")
    conn.commit()
    cursor.execute("SELECT * FROM logs;")
    print(cursor.fetchall())
    cursor.close()
    conn.close()

if __name__ == "__main__":
    write_read()
