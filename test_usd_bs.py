import mysql.connector 
import sys
import test_edit as ed
import bcv
tasa=bcv.tasaf()
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="test"
)

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
        newbsd=cambio*tasa
        print(f"Estarías cambiando {cambio} por {newbsd}")
        comp=input("Estas seguro de continuar?[Y/N]")
        if comp=="y" or comp=="Y":
            print("Reto aceptado")
            cant=newbs[3]+newbsd
            oldcant=oldusd[3]-cambio
            return newbs[2],newbs[4],cant,oldusd[2],oldusd[4],oldcant,usuario
        else:sys.exit(0)
    else:
        print("Saldo Insuficiente o cifra ridicula")
        sys.exit(0)

to_upd=cambio_bs(usuario,tasa)
ed.reg_bd(to_upd[0],to_upd[1],to_upd[2],to_upd[3],to_upd[4],to_upd[5],to_upd[6])