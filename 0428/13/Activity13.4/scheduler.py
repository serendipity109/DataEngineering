from threading import Timer
import time
import mysqldb
import mongodb
import redisdb
# Activity 13.5: import cassandradb
import sys

def clearout():
    mysqldb.delete()
    mongodb.delete()
    redisdb.delete()
    # Activity 13.5: cassandradb.delete()
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

def verify():
    stamps = mongodb.read()
    status(stamps, 'mongo')
    lastInsertDate = redisdb.read()
    print(f'Data in Redis: LastInsertDate = {lastInsertDate.decode("utf-8")}')
    # Activity 13.5: cassandradb.read()

def timeloop():
    print(f'--- LOOP: {time.ctime()} ---')
    mysql()
    mongo()
    redis()
    verify()
    Timer(5, timeloop).start()

timeloop()
