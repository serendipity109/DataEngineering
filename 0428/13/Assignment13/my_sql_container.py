import argparse
import docker

def create_mysql():
    client = docker.from_env()
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
    client = docker.from_env()
    try:
        c = client.containers.get("final_mysql_container")
        c.remove(force=True)
        print("MySQL container removed.")
    except docker.errors.NotFound:
        print("MySQL container not found.")

if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("action", choices=["create", "delete"])
    args = p.parse_args()
    if args.action == "create":
        create_mysql()
    else:
        delete_mysql()
