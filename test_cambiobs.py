import mysql.connector
import sys
import test_edit as ed

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="test"
)

bcv=float(36.23)
usuario="ZRO-42111"
crs=mydb.cursor()

def cambio_dlr(usuario,tasa,dispo):
   print(f"{usuario} + {tasa} + {dispo}")
   sql=f"SELECT * FROM `billetera` WHERE `poseedor`='{usuario}' AND  `tipo`='USD' "
   crs.execute(sql)
   inf=crs.fetchone()
   sql=f"SELECT * FROM `billetera` WHERE `poseedor`='{usuario}' AND  `tipo`='Bs.D' "
   crs.execute(sql)
   det=crs.fetchone()
   print(f"Tasa del día: {tasa}")
   cambio=float(input(f"Ingrese cuanto {det[2]} desea cambiar: "))
   cant_max=det[3]
   cant_min=tasa*5
   if cambio>cant_min and cambio<cant_max:
        new= cambio/tasa
        print(f"Estarías comprando: {new}")
        newcry=new+float(inf[3])
        newus=cant_max-cambio
        print(f"{newcry}+{newus}")
        id1=inf[4]
        id2=det[4]
        salida=('USD','Bs.D',id1,id2,newcry,newus,usuario)
        print(salida)
        return list(salida)
   else: 
        print("JAJAAJAAJ, No tienes suficiente saldo, o peor, no vas a comprar lo suficiente XDDD")
        sys.exit(0)

to_upd=cambio_dlr(usuario,bcv,1)
ed.reg_bd(to_upd[0],to_upd[1],to_upd[2],to_upd[3],to_upd[4],to_upd[5],to_upd[6])
