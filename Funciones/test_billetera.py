import mysql.connector
import sys

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="test"
)
def comp(parametro):
    cursor1=mydb.cursor()
    sql=f"SELECT `billeteraID` FROM `billetera` WHERE `billeteraID`='{parametro}'"
    cursor1.execute(sql)
    myresult = cursor1.fetchone()
    if myresult:
        for x in myresult:
            print(f"{parametro} Billetera Registrada")
            print(x)
            sys.exit(0)
    else:
        print(f"Disponible: {parametro}")
usuario="EZr-24018"
def reg_b():
    cursor1=mydb.cursor()
    sql=f"SELECT `UserID` FROM `usuario` WHERE `UserID`='{usuario}'"
    cursor1.execute(sql)
    myresult = cursor1.fetchone()
    sel=input("""
    Seleccione que tipo de billetera crear:
    - 1. Bs.D
    - 2. $$$$
    - 3. Cripto
    ->  """)
    if int(sel)==1:
        newB=f"{myresult[0]}-BSD"
        cursor1=mydb.cursor()
        comp(newB)
        sql="INSERT INTO `billetera`(`poseedor`, `tipo`, `cantidad`, `billeteraID`) VALUES (%s,%s,%s,%s)"
        entrada=(usuario,'Bs.D',0,newB)
        cursor1.execute(sql,entrada)
        mydb.commit()
        mydb.close()
    elif int(sel)==2:
        newB=f"{myresult[0]}-USD"
        cursor1=mydb.cursor()
        comp(newB)
        sql="INSERT INTO `billetera`(`poseedor`, `tipo`, `cantidad`, `billeteraID`) VALUES (%s,%s,%s,%s)"
        entrada=(usuario,'USD',0,newB)
        cursor1.execute(sql,entrada)
        mydb.commit()
        mydb.close()
    elif int(sel)==3:
        newB=f"{myresult[0]}-CRYPTO"
        cursor1=mydb.cursor()
        comp(newB)
        sql="INSERT INTO `billetera`(`poseedor`, `tipo`, `cantidad`, `billeteraID`) VALUES (%s,%s,%s,%s)"
        entrada=(usuario,'CRYPTO',0,newB)
        cursor1.execute(sql,entrada)
        mydb.commit()
        mydb.close()
    else:
        print("OTROO")
reg_b()