import mysql.connector 
def fixhistory(user):
    while True:
        mydb=mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="test"
        )
        crs=mydb.cursor()
        sql=f"SELECT * FROM `historial` WHERE `servidor`='{user}' OR `recep`='{user}'"
        crs.execute(sql)
        inf_history=crs.fetchall()
        return inf_history