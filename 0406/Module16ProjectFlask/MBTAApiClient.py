import urllib.request
import json
import mysqldb
from datetime import datetime

def callMBTAApi():
    mbtaDictList = []
    mbtaUrl = 'https://api-v3.mbta.com/vehicles?filter[route]=1&include=trip'
    with urllib.request.urlopen(mbtaUrl) as url:
        data = json.loads(url.read().decode())
        for bus in data['data']:
            busDict = {
                'id': bus['id'],
                'latitude': bus['attributes']['latitude'],
                'longitude': bus['attributes']['longitude'],
                'bearing': bus['attributes'].get('bearing'),
                'current_status': bus['attributes'].get('current_status'),
                'current_stop_sequence': bus['attributes'].get('current_stop_sequence'),
                'occupancy_status': bus['attributes'].get('occupancy_status'),
                'updated_at': datetime.strptime(bus['attributes']['updated_at'], '%Y-%m-%dT%H:%M:%S%z') if bus['attributes'].get('updated_at') else None
            }
            mbtaDictList.append(busDict)
    mysqldb.insertMBTARecord(mbtaDictList)

    return mbtaDictList
