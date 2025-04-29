import docker

client = docker.from_env()

def create_cassandra():
    client.containers.run(
        image="cassandra:4.0",
        name="final_cassandra_container",
        ports={"9042/tcp": 1000},
        detach=True
    )
    print("Cassandra container created: final_cassandra_container on port 1000")

if __name__ == "__main__":
    import sys
    if "create" in sys.argv:
        create_cassandra()
    else:
        print("Usage: python my_cassandra_container.py create")
