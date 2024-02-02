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
selec="CRYPTO"
crp=47
crs=mydb.cursor()
def main():
    sql=f"SELECT `tipo`, `cantidad` FROM `billetera` WHERE `poseedor`='{usuario}'"
    crs.execute(sql)
    all=crs.fetchall()
    print("Seleccione tipo de billetera al cambio: ")
    f=0
    ops=set()
    for bill in all :
        f+=1
        if not selec==bill[0]:
            print(f"- {f}. {bill[0]} (Saldo disponible: {bill[1]})")
            ops.add((bill[0],float(bill[1]),f))
        else: continue
    print(ops)
    new=input("-> ")
    for op in ops:
        if int(new)==op[2] and op[0]=="Bs.D":
            print("a")
        elif int(new)==op[2] and op[0]=="USD":
            print("b")

def cambio_personalizado(pers,ops):
    for op in ops:
        maxi=op[1]/7
        enter=input(f"""
Tiene un total de {op[1]} disponible, cuanto desea cambiar?
->
""")
        if enter<=pers:
            llave=enter/pers
            key=llave-op[1]
            sql=f"UPDATE `billetera` SET `cantidad`='{llave}' WHERE `poseedor`= '{usuario}' AND `tipo`='{selec}'"
            sqlP=f"UPDATE `billetera` SET `cantidad`='{key}' WHERE `poseedor`= '{usuario}' AND `tipo`='{op[0]}'"
            crs.execute(sql)
            crs.execute(sqlP)
            mydb.commit()
mydb.close()