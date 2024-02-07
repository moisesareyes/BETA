import mysql.connector
import sys
import test_edit as ed 

mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='test'
)

crs=mydb.cursor()
bcv=float(36.23)
usuario="ZRO-42111"

def cambio_cry(usuario,tasa, dispo):
    sql=f"SELECT * FROM `billetera` WHERE `poseedor`='{usuario}' AND  `tipo`='Bs.D' "
    crs.execute(sql)
    inf=crs.fetchone()
    sql=f"SELECT * FROM `billetera` WHERE `poseedor`='{usuario}' AND  `tipo`='USD' "
    crs.execute(sql)
    det=crs.fetchone()
    print(f"{inf} vs {det}")
    cant_max=float(det[3])
    print(tasa)
    print(f"{cant_max} + {5}")
    cambio=float(input(f"Ingrese cuanto {det[2]} desea cambiar: "))
    if cambio>5 and cambio<cant_max:
        new= cambio*tasa
        print(new)
        newcry=new+float(inf[3])
        newus=cant_max-cambio
        print(f"{newcry}+{newus}")
        id1=inf[4]
        id2=det[4]
        salida=('USD','Bs. D',id1,id2,newus,newcry,usuario)
        print(salida)
        return list(salida)
    else: 
        print("JAJAAJAAJ, No tienes suficiente saldo, o peor, no vas a comprar lo suficiente XDDD")
        sys.exit(0)


to_upd=cambio_cry(usuario,bcv,1)
ed.reg_bd(to_upd[0],to_upd[1],to_upd[2],to_upd[3],to_upd[4],to_upd[5],to_upd[6])
