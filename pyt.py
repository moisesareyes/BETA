import mysql.connector

test1=input("Ingrese un nombre: ")
test2=input("Ingrese una contraseña: ")

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="test"
)
cursor1=mydb.cursor()
info_test=(test1,test2)
sql="INSERT INTO `test`(`user`, `pass`) VALUES (%s,%s)"
cursor1.execute(sql,info_test)
mydb.commit()
mydb.close()