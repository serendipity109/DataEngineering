from cassandra.cluster import Cluster

cluster = Cluster(['127.0.0.1'], port=9042)
session = cluster.connect()

session.execute("""
    CREATE KEYSPACE IF NOT EXISTS books
    WITH replication = { 'class': 'SimpleStrategy', 'replication_factor': '1' }
""")

session.set_keyspace('books')

session.execute("""
    CREATE TABLE IF NOT EXISTS book (
        Book_ID int PRIMARY KEY,
        Name text,
        Author text,
        Year_Published int,
        Number_of_Pages int
    )
""")

print("Keyspace 'books' and table 'book' are ready.")
