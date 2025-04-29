import time
from mysqldb import write_read as mysql_op
from mongodb import write_read as mongo_op

def scheduler(interval=5, runs=10):
    for i in range(runs):
        print(f"[{i+1}] MySQL operation:")
        mysql_op()
        print(f"[{i+1}] MongoDB operation:")
        mongo_op()
        time.sleep(interval)

if __name__ == "__main__":
    scheduler(interval=10, runs=5)
