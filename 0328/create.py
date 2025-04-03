import mysql.connector
import sys
sys.dont_write_bytecode = True

cnx = mysql.connector.connect(user='root', 
    password='MyNewPass',
    host='127.0.0.1',
    port="3300",
    database='',
    auth_plugin='mysql_native_password')

# create cursor
cursor = cnx.cursor()

# delete previous db
query = ("DROP DATABASE IF EXISTS `restaurants`;")
cursor.execute(query)

# create db
query = ("CREATE DATABASE IF NOT EXISTS restaurants")
cursor.execute(query)

# use db
query = ("USE restaurants")
cursor.execute(query)

# create table
query = ('''
CREATE TABLE restaurant(
    id VARCHAR(36),
    stamp VARCHAR(20),
    name VARCHAR(20),
    type VARCHAR(20)
)
''')
cursor.execute(query)

# clean up
cnx.commit()
cursor.close()
cnx.close()    