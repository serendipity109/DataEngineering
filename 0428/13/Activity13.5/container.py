import os
import sys
import pymysql
from cassandra.cluster import Cluster

# ----------------
# input arguments
# ----------------
# -delete, delete containers    
# -create, create containers
# -init, init mysql, mongodb does not need it

# delete containers
def delete(container):
    cmd = f'docker stop {container}'
    result = os.system(cmd)
    if result == 0:
        os.system(f'docker rm {container}')
        print(f'Removed {container}')

# create container
def create(cmd, db):
    result = os.system(cmd)
    if result == 0:
        print(f'Created {db}')

# initialize mysql db
def init_mysql():
    cnx = pymysql.connect(user='root', 
                           password='MyNewPass',
                           host='127.0.0.1')
    cursor = cnx.cursor()
    cursor.execute("DROP DATABASE IF EXISTS `pluto`;")
    cursor.execute("CREATE DATABASE IF NOT EXISTS pluto;")
    cursor.execute("USE pluto;")
    cursor.execute('''
        CREATE TABLE posts(
            id VARCHAR(36),
            stamp VARCHAR(20)
        );
    ''')
    cnx.commit()
    cursor.close()
    cnx.close()

# initialize cassandra db
def init_cassandra():
    keyspace = None
    cluster = Cluster(['localhost'], port=9042)
    session = cluster.connect(keyspace)
    session.execute("""
        CREATE KEYSPACE IF NOT EXISTS stamps
        WITH REPLICATION = {'class':'SimpleStrategy','replication_factor':1};
    """)
    session.set_keyspace('stamps')
    session.execute("""
        CREATE TABLE IF NOT EXISTS posts (
            id text PRIMARY KEY,
            stamp text
        );
    """)
    session.execute("""
        INSERT INTO posts (id, stamp)
        VALUES ('maxTimeStamp', '1975-01-01 00:00:00')
        IF NOT EXISTS;
    """)


# read input argument
argument = sys.argv[1] if len(sys.argv) > 1 else None

if argument == '-delete':
    delete('some-mysql')
    delete('some-mongo')
    delete('some-redis')
    delete('some-cassandra')
    sys.exit()

if argument == '-create':
    create('docker run -p 3306:3306 --name some-mysql -e MYSQL_ROOT_PASSWORD=MyNewPass -d mysql', 'mysql')
    create('docker run -p 27017:27017 --name some-mongo -d mongo', 'mongo')
    create('docker run -p 6379:6379 --name some-redis -d redis', 'redis')
    create('docker run -p 9042:9042  --name some-cassandra -d cassandra', 'cassandra')
    sys.exit()

if argument == '-init':
    init_mysql()
    init_cassandra()
    sys.exit()
