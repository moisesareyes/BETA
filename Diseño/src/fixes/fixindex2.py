import mysql.connector
def indexforbilletera(user):
    while True:
        mydb=mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="test"
        )
        sql=f"SELECT `id`, `poseedor`, `tipo`, `cantidad`, `billeteraID`, `act` FROM `billetera` WHERE`poseedor`='{user}'"
        crs=mydb.cursor()
        crs.execute(sql)
        inf_bill=crs.fetchall()
        return inf_bill