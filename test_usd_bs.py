import mysql.connector 
import sys
import test_edit as ed
#import bcv

#tasa=bcv.tasa
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="test"
)
bcv=36.29
usuario="ZRO-42111"
crs=mydb.cursor()

def cambio_bs(usuario,tasa):
    sql=f"SELECT * FROM `billetera` WHERE `poseedor`='{usuario}' AND  `tipo`='Bs.D' "
    crs.execute(sql)
    newbs=crs.fetchone()
    sql=f"SELECT * FROM `billetera` WHERE `poseedor`='{usuario}' AND  `tipo`='USD' "
    crs.execute(sql)
    oldusd=crs.fetchone()
    print(f"{newbs}v{oldusd}")
    maxi=oldusd[3]*tasa
    mini=5
    print(f"Tienes un total de {oldusd[3]} {oldusd[2]}, lo que equivale a {maxi} {newbs[2]}")
    print(f"Por ley, transferencias de minimo 5 USD")
    cambio=float(input(f"Cuantos {oldusd[2]} desea cambiar? "))
    if cambio>=mini and maxi>=cambio:
        newbs=cambio*tasa
        print(f"Estarías cambiando {cambio} por {newbs}")
        comp=("Estas seguro de continuar?[Y/N]")
        if comp=="y" or comp=="Y":
            print("Reto aceptado")
        else:sys.exit(0)
    else:
        print("Saldo Insuficiente o cifra ridicula")
        sys.exit(0)

cambio_bs(usuario,bcv)