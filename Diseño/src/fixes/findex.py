import mysql.connector
def indexforuser(user):
    while True:
        mydb=mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="test"
        )
        crs=mydb.cursor()
        sql=f"SELECT `ID`, `UserID`, `Nombre`, `Apellido`, `User_name`, `Email`, `Pass`, `Tlf`, `Reg` FROM `usuario` WHERE `UserID`='{user}'"
        crs.execute(sql)
        inf_usr=crs.fetchone()
        return inf_usr