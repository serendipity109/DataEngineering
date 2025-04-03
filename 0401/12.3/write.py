# pip install redis
import redis
from datetime import datetime

# connect to server
r = redis.Redis(host='localhost', port=6379, db=0)

# write to server
t = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
r.rpush('nums', t)

# use mset to write multiple keys
r.mset({'Italy': 'Rome', 'France': 'Paris'})
