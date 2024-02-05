import mysql.connector
import sys

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="test"
)

bcv=float(36.23)
usuario="ZRO-42111"
tipo="CRYPTO"
crp=47
crs=mydb.cursor()
def cambio_cry(usuario, tipo,tasa, dispo):
    sql=f"SELECT * FROM `billetera` WHERE `poseedor`='{usuario}' AND  `tipo`='{tipo}' "
    crs.execute(sql)
    inf=crs.fetchone()
    sql=f"SELECT * FROM `billetera` WHERE `poseedor`='{usuario}' AND  `tipo`='USD' "
    crs.execute(sql)
    det=crs.fetchone()
    print(f"{inf} vs {det}")
    if det[2]=="Bs.D" and tipo=="CRYPTO": 
         print("NO SE PUEDEN COMPRAR CRYPTOS CON BOLIVARES")
         sys.exit(0)
    cant_max=float(det[3])
    print(tasa)
    print(f"{cant_max} + {5}")
    cambio=float(input(f"Ingrese cuanto {det[2]} desea cambiar: "))
    if cambio>5 and cambio<cant_max:
        new= cambio/tasa
        print(new)
#cambio_cry(usuario,tipo,42500.38,1)
#################################### Bolivar a $$$$
def cambio_dlr(usuario,tasa,dispo):
    print(f"{usuario} + {tasa} + {dispo}")
cambio_dlr(usuario,bcv,10000)
mydb.close()