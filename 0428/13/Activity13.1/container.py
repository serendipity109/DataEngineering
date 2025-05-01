import argparse
import docker
from docker.errors import NotFound, APIError

client = docker.from_env()

def create_mysql():
    print("Creating MySQL container...")
    client.containers.run(
        "mysql:latest",
        name="final_mysql_container",
        ports={"3306/tcp": 5600},
        environment={
            "MYSQL_ROOT_PASSWORD": "rootpass",
            "MYSQL_DATABASE": "testdb"
        },
        detach=True
    )
    print("MySQL container created.")

def delete_mysql():
    print("Deleting MySQL container...")
    try:
        c = client.containers.get("final_mysql_container")
        c.remove(force=True)
        print("MySQL container removed.")
    except NotFound:
        print("MySQL container not found.")

def create_mongo():
    print("Creating MongoDB container...")
    client.containers.run(
        "mongo:latest",
        name="final_mongo_container",
        ports={"27017/tcp": 27017},
        detach=True
    )
    print("MongoDB container created.")

def delete_mongo():
    print("Deleting MongoDB container...")
    try:
        c = client.containers.get("final_mongo_container")
        c.remove(force=True)
        print("MongoDB container removed.")
    except NotFound:
        print("MongoDB container not found.")

def create_redis():
    print("Creating Redis container...")
    client.containers.run(
        "redis:latest",
        name="final_redis_container",
        ports={"6379/tcp": 6379},
        detach=True
    )
    print("Redis container created.")

def delete_redis():
    print("Deleting Redis container...")
    try:
        c = client.containers.get("final_redis_container")
        c.remove(force=True)
        print("Redis container removed.")
    except NotFound:
        print("Redis container not found.")

def create_cassandra():
    print("Creating Cassandra container...")
    client.containers.run(
        "cassandra:latest",
        name="final_cassandra_container",
        ports={"9042/tcp": 9042},
        detach=True
    )
    print("Cassandra container created.")

def delete_cassandra():
    print("Deleting Cassandra container...")
    try:
        c = client.containers.get("final_cassandra_container")
        c.remove(force=True)
        print("Cassandra container removed.")
    except NotFound:
        print("Cassandra container not found.")

def main():
    p = argparse.ArgumentParser(description="Create or delete database containers")
    p.add_argument("action", choices=["create", "delete"],
                   help="create: run containers; delete: remove containers")
    args = p.parse_args()

    if args.action == "create":
        create_mysql()
        create_mongo()
        create_redis()
        create_cassandra()
    else:
        # 反序刪除可確保彼此之間 network 依賴較小
        delete_cassandra()
        delete_redis()
        delete_mongo()
        delete_mysql()

if __name__ == "__main__":
    try:
        main()
    except APIError as e:
        print(f"Docker API error: {e.explanation}")
