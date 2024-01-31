import mysql.connector
import sys
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="test"
)
def comp(para,metro):
    cursor1=mydb.cursor()
    sql=f"SELECT `{para}` FROM `usuario` WHERE `{para}`='{metro}'"
    cursor1.execute(sql)
    myresult = cursor1.fetchone()
    if myresult:
        for x in myresult:
            print("Usado")
            print(x)
            sys.exit(0)
    else:
        print(f"Disponible: {metro}")
def cont(contar,long):
    testC=len(long)
    if testC<contar:
        print(f"Necesitas ma' viejo noma, minimo: {long}")
        sys.exit(0)
def char(ctr):
    nums = [caracter.isdigit() for caracter in ctr]
    print(f"Numeros: {any(nums)}")
    strs= [caracter.isalpha() for caracter in ctr]
    print(f"Letras: {any(strs)}")
    mayus= [caracter.isupper() for caracter in ctr]
    print(f"Mayúsculas: {any(mayus)}")
    minus= [caracter.islower() for caracter in ctr]
    print(f"Mayúsculas: {any(minus)}")

    if any(nums) is False or any(strs) is False or any(mayus) is False or any(minus) is False:
        print("Use mayúsculas, minusculas y numeros")
        sys.exit(0)
#Nombre, Apellido, User_name, Email, Pass, Tlf, Reg	
def reg():
    test1=input("Ingrese su nombre: ")
    test2=input("Ingrese su apellido: ")
    test3=input("Ingrese su Username: ")
    comp('User_name',test3)
    cont(5,test3)
    test4=input("Ingrese su Email: ")
    comp('Email',test4)
    test5=input("Ingrese su contraseña: ")
    char(test5)
    cont(8,test5)
    test5_2=input("Repita su contraseña: ")
    if not test5==test5_2: print ("Revise las contraseñas"), sys.exit(0)
    test6=input("Ingrese su numero de telefono: ")
    comp('Tlf',test6)
    info_test=(test1,test2,test3,test4,test5,test6)
    return info_test
cursor1=mydb.cursor()
sql="INSERT INTO `usuario`(`Nombre`, `Apellido`, `User_name`, `Email`, `Pass`, `Tlf`) VALUES (%s,%s,%s,%s,%s,%s)"
cursor1.execute(sql,reg())
mydb.commit()
mydb.close()