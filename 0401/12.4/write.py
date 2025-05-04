from cassandra.cluster import Cluster

cluster = Cluster(['127.0.0.1'], port=9042)
session = cluster.connect()

session.execute("""
    CREATE KEYSPACE IF NOT EXISTS books
    WITH REPLICATION = {
        'class': 'SimpleStrategy',
        'replication_factor': 1
    };
""")

session.set_keyspace('books')

session.execute("""
    CREATE TABLE IF NOT EXISTS book (
        book_id          int PRIMARY KEY,
        name             text,
        author           text,
        year_published   int,
        number_of_pages  int
    );
""")

books = [
    (1, 'The Mystery of Capital', 'Hernando de Soto',      1970, 209),
    (2, 'Fairy Tales',            'Hans Christian Andersen',1836, 784),
    (3, 'The Divine Comedy',      'Dante Alighieri',        1315, 928),
    (4, 'Romeo and Juliet',       'William Shakespeare',    1597, 100),
]

insert_stmt = session.prepare("""
    INSERT INTO book (book_id, name, author, year_published, number_of_pages)
    VALUES (?, ?, ?, ?, ?)
""")

for b in books:
    session.execute(insert_stmt, b)

cluster.shutdown()
