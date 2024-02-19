import mysql.connector 
import sys

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="test"
)
crs=mydb.cursor()
def hist (usuario,receptor,tipo,moneda,status,cantidad):
    ##LUEGOOOOO
    print("a")
# INSERT INTO `historial`(`ID`, `servidor`, `recep`, `tipo`, `moneda`, `status`, `cantidad`, `billetera1`, `billetera2`, `fecha`) VALUES ('[value-1]','[value-2]','[value-3]','[value-4]','[value-5]','[value-6]','[value-7]','[value-8]','[value-9]','[value-10]')