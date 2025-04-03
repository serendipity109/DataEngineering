# pip install redis
import redis

# connect to server
r = redis.Redis(host='localhost', port=6379, db=0)

# read list items
for item in r.lrange('nums', 0, -1):
    print(item)

# read values from mset keys
italy = r.get('Italy')
france = r.get('France')

print(f"Italy: {italy}")
print(f"France: {france}")
