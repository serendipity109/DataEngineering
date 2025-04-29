import docker

client = docker.from_env()

def create_mongo():
    client.containers.run(
        image="mongo:latest",
        name="final_mongo_container",
        ports={"27017/tcp": 1800},
        detach=True
    )
    print("MongoDB container created: final_mongo_container on port 1800")

if __name__ == "__main__":
    import sys
    if "create" in sys.argv:
        create_mongo()
    else:
        print("Usage: python my_mongo_container.py create")
