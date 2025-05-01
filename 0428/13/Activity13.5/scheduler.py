from threading import Timer
import time
import mysqldb
import mongodb
import redisdb
import cassandradb
import sys

def clearout():
    mysqldb.delete()
    mongodb.delete()
    redisdb.delete()
    cassandradb.delete()
    print('Deleted data in all dbs!')

arg = sys.argv[1] if len(sys.argv) > 1 else None
if arg == '-clear':
    clearout()
    sys.exit()

def status(stamps, db):
    print(f'Data in {db}:')
    for s in stamps:
        print(s)
    time.sleep(2)

def mysql():
    mysqldb.write()

def mongo():
    stamps = mysqldb.read()
    status(stamps, 'mysql')
    mongodb.write(stamps)

def redis():
    stamps = mysqldb.read()
    redisdb.write(stamps)

def cassandra():
    stamps = mysqldb.read()
    cassandradb.write(stamps)

def verify():
    stamps = mongodb.read()
    status(stamps, 'mongo')
    lastInsertDate = redisdb.read()
    print(f'Data in Redis: LastInsertDate = {lastInsertDate.decode("utf-8")}')
    lastUpdateDate = cassandradb.read()
    print(f'Data in Cassandra: LastUpdateDate = {lastUpdateDate}')

def timeloop():
    print(f'--- LOOP: {time.ctime()} ---')
    mysql()
    mongo()
    redis()
    cassandra()
    verify()
    Timer(5, timeloop).start()

timeloop()
