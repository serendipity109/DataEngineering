import mysql.connector

def insertMBTARecord(mbtaList):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="MyNewPass",
        database="MBTAdb"
    )

    mycursor = mydb.cursor()
    sql = """
    INSERT INTO mbta_buses (
        id, trip_id, direction_id, label, stop_id,
        latitude, longitude, bearing, current_status,
        current_stop_sequence, occupancy_status, updated_at
    ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    for mbtaDict in mbtaList:
        val = (
            mbtaDict['id'],
            mbtaDict.get('trip_id'),
            mbtaDict.get('direction_id'),
            mbtaDict.get('label'),
            mbtaDict.get('stop_id'),
            mbtaDict['latitude'],
            mbtaDict['longitude'],
            mbtaDict.get('bearing'),
            mbtaDict.get('current_status'),
            mbtaDict.get('current_stop_sequence'),
            mbtaDict.get('occupancy_status'),
            mbtaDict.get('updated_at')
        )
        mycursor.execute(sql, val)

    mydb.commit()
    mycursor.close()
    mydb.close()