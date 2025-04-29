import docker

client = docker.from_env()

def create_redis():
    client.containers.run(
        image="redis:7.0",
        name="final_redis_container",
        ports={"6379/tcp": 2400},
        detach=True
    )
    print("Redis container created: final_redis_container on port 2400")

if __name__ == "__main__":
    import sys
    if "create" in sys.argv:
        create_redis()
    else:
        print("Usage: python my_redis_container.py create")
