import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="test"
)


#INSERT INTO `billetera`(`id`, `poseedor`, `tipo`, `cantidad`, `billeteraID`, `act`) VALUES ('[value-1]','[value-2]','[value-3]','[value-4]','[value-5]','[value-6]')
