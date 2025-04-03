import mysql.connector

def insertMBTARecord(mbtaList):
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="MyNewPass",
    database="MBTAdb"
    )

    mycursor = mydb.cursor()
    #complete the following line to add all the fields from the table
    sql = "insert into mbta_buses ( id, longitude, latitude) values (%s, %s,%s)"
    for mbtaDict in mbtaList:
        #complete the following line to add all the fields from the table
        val = (mbtaDict['id'], mbtaDict['label'], mbtaDict['longitude'])
        mycursor.execute(sql, val)

    mydb.commit()