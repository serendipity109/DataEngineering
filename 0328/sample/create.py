import mysql.connector
import sys
sys.dont_write_bytecode = True

cnx = mysql.connector.connect(user='root', 
    password='MyNewPass',
    host='127.0.0.1',
    database='',
    auth_plugin='mysql_native_password')

# create cursor
cursor = cnx.cursor()

# delete previous db
query = ("DROP DATABASE IF EXISTS `pluto`;")
cursor.execute(query)

# create db
query = ("CREATE DATABASE IF NOT EXISTS pluto")
cursor.execute(query)

# use db
query = ("USE pluto")
cursor.execute(query)

# create table
query = ('''
CREATE TABLE posts(
    id VARCHAR(36),
    stamp VARCHAR(20)
)
''')
cursor.execute(query)

# clean up
cnx.commit()
cursor.close()
cnx.close()    