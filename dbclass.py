import mysql.connector

def getconn():
    conn=mysql.connector.connect(
        host="localhost",
        username="root",
        password="siva@123",
        port=3306,
        database="mydb")
    return conn

def fetchAll(sql):
    conn=getconn()
    cursor=conn.cursor()
    cursor.execute(sql)
    data=cursor.fetchall()
    return data
def executeUpdate(sql):
    conn = getconn()
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()
    return True