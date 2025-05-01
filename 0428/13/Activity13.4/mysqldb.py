import pymysql
from datetime import datetime
import atexit
import uuid

cnx = pymysql.connect(user='root', 
                      password='MyNewPass',
                      host='127.0.0.1',
                      db='pluto')
cursor = cnx.cursor()

def write():
    id = str(uuid.uuid4())
    time_str = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    cursor.execute(f'INSERT INTO posts VALUES("{id}","{time_str}")')
    cnx.commit()

def read():
    cursor.execute("SELECT * FROM posts ORDER BY stamp DESC LIMIT 5;")
    return [row[1] for row in cursor.fetchall()]

def delete():
    cursor.execute("TRUNCATE posts;")
    cnx.commit()

@atexit.register
def exit_handler():
    cursor.close()
    cnx.close()
