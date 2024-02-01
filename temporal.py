import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="test"
)
ap="Eddie"
ap2="0424-7060"
ap3=ap[0]+ap[2]+ap[4]+"-"+ap2[2]+ap2[3]+ap2[-1]+ap2[-2]+ap2[-3]
print(ap3)
control=list()
ctr=("WOW ES EL 10")
nums = [caracter.isdigit() for caracter in ctr]
control.append(any(nums))
print(f"Numeros: {any(nums)}")
strs= [caracter.isalpha() for caracter in ctr]
print(f"Letras: {any(strs)}")
control.append(any(strs))
mayus= [caracter.isupper() for caracter in ctr]
print(f"Mayúsculas: {any(mayus)}")
control.append(any(mayus))
print(control)
minus= [caracter.islower() for caracter in ctr]
print(f"Minusculas: {any(minus)}")

test=input("TA: ")
testC=len(test)
if testC<5:
    print("Necesitas more viejo noma")

email=input("Ingrese su Email: ")
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="test"
)
cursor1=mydb.cursor()
sql=f"SELECT `Email` FROM `usuario` WHERE `Email`='{email}'"
cursor1.execute(sql)
myresult = cursor1.fetchone()
if myresult:
    for x in myresult:
        print("Email usado")
        print(x)
else:
    print(f"Nombre disponible: {email}")
mydb.close()