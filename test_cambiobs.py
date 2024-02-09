import mysql.connector
import sys
import test_edit as ed
#import bcv
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="test"
)
#pr=bcv.tasa
#print(pr)
tasa=int(36.23)
usuario="ZRO-42111"
crs=mydb.cursor()

def cambio_dlr(usuario,tasa):
   print(f"{usuario} + {tasa}")
   sql=f"SELECT * FROM `billetera` WHERE `poseedor`='{usuario}' AND  `tipo`='USD' "
   crs.execute(sql)
   newm=crs.fetchone()
   sql=f"SELECT * FROM `billetera` WHERE `poseedor`='{usuario}' AND  `tipo`='Bs.D' "
   crs.execute(sql)
   oldc=crs.fetchone()
   maxi=oldc[3]/tasa
   mini=5
   minix2=5*tasa
   print(f"Tienes un total de {oldc[3]}{oldc[2]} disponible, lo que equivale a {int(maxi)} {newm[2]}")
   print(f"Debes comprar un minimo de 5 {newm[2]}, equivalente a {minix2} {oldc[2]}")
   cambio=float(input(f"Cuanto {newm[2]} desea comprar?: "))
   if cambio>=mini and maxi>=cambio:
      newpre=cambio*tasa
      rep=input(f"Estarías cambiando {newpre}{oldc[2]} por {cambio}{newm[2]}, estás seguro?[Y/N]: ")
      if rep=="Y" or rep=="y":
         cant=newm[3]+cambio
         oldcant=oldc[3]-newpre
         return newm[2],newm[4],cant,oldc[2],oldc[4],oldcant,usuario
      else:sys.exit(0)
   else:
      print("Saldo insuficiente... ")
      sys.exit(0)

to_upd=cambio_dlr(usuario,tasa)
ed.reg_bd(to_upd[0],to_upd[1],to_upd[2],to_upd[3],to_upd[4],to_upd[5],to_upd[6])
