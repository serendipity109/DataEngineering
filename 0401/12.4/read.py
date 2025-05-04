from cassandra.cluster import Cluster


cluster = Cluster(['127.0.0.1'], port=9042)
session = cluster.connect('books')

rows = session.execute("SELECT * FROM book;")

for row in rows:
    print(f"{row.book_id:>2}: {row.name} ─ {row.author} "
          f"({row.year_published}) | {row.number_of_pages} pages")

cluster.shutdown()
