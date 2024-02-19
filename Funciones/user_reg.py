import mysql.connector
import sys
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="test"
)
crs=mydb.cursor()

def reg_user(nombre,apellido,usuario,email,passw,tlf):
    id=usuario[0]+usuario[2]+usuario[4]+"-"+tlf[2]+tlf[3]+tlf[-3]+tlf[-2]+tlf[-1]
    inputs=(id,nombre,apellido,usuario,email,passw,tlf)
    sql="INSERT INTO `usuario`(`UserID`,`Nombre`, `Apellido`, `User_name`, `Email`, `Pass`, `Tlf`) VALUES (%s,%s,%s,%s,%s,%s,%s)"
    crs.execute(sql,inputs)
    mydb.commit()

mydb.close()