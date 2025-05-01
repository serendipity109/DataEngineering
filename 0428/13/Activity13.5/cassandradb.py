from cassandra.cluster import Cluster

keyspace = 'stamps'
cluster = Cluster(['localhost'], port=9042)
session = cluster.connect(keyspace)

def write(stamps):
    sql = f"UPDATE posts SET stamp = '{stamps[0]}' WHERE id = 'maxTimeStamp' IF EXISTS"
    session.execute(sql)

def read():
    result = session.execute("SELECT stamp FROM posts WHERE id = 'maxTimeStamp'")
    return result.one().stamp

def delete():
    session.execute("DELETE FROM posts WHERE id = 'maxTimeStamp'")
