import mysql.connector
import datetime as dt
import sys

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="test"
)
crs=mydb.cursor()
usuario='EZr-24018'
doc=input("Cedula: ")
tipo="Bs.D"
banco='0102'
tlf=input("Telefono: ")
fecha= dt.date.today()
ref=20000000
print(fecha)
def recarga(usuario,doc,tipo,banco,tlf,cant,fecha,ref):
    new=(usuario,tipo,doc,banco,tlf,cant,ref,"Pendiente",fecha)
    sql="INSERT INTO `recarga`(`usuario`, `tipo`, `doc`, `banco`, `telefono`, `cantidad`, `operacion`, `status`, `fecha_tra`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    crs.execute(sql,new)
    mydb.commit()
recarga(usuario,doc,tipo,banco,tlf,fecha,ref)
