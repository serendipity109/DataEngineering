import docker

client = docker.from_env()

def create_all():
    # MySQL
    client.containers.run(
        "mysql:8.0", name="final_mysql_container",
        ports={"3306/tcp": 5600},
        environment={"MYSQL_ROOT_PASSWORD":"root","MYSQL_DATABASE":"testdb"},
        detach=True
    )
    # MongoDB
    client.containers.run(
        "mongo:5.0", name="final_mongo_container",
        ports={"27017/tcp": 1800},
        detach=True
    )
    # Redis
    client.containers.run(
        "redis:7.0", name="final_redis_container",
        ports={"6379/tcp": 2400},
        detach=True
    )
    # Cassandra
    client.containers.run(
        "cassandra:4.0", name="final_cassandra_container",
        ports={"9042/tcp": 1000},
        detach=True
    )
    print("All 4 containers created.")

if __name__ == "__main__":
    import sys
    if "-init" in sys.argv:
        create_all()
    else:
        print("Usage: python container.py -init")
