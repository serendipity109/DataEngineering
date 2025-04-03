import mysql.connector
from datetime import datetime
import uuid
import sys
sys.dont_write_bytecode = True

cnx = mysql.connector.connect(user='root', 
    password='MyNewPass',
    host='127.0.0.1',
    database='pluto',
    auth_plugin='mysql_native_password')

# create cursor
cursor = cnx.cursor()

# insert
query = ("SELECT * FROM posts")
cursor.execute(query)

for row in cursor.fetchall():
    print(row)

# clean up
cursor.close()
cnx.close()    