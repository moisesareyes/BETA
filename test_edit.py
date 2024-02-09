def reg_bd(atc,id1,cant_act,old,id2,cant_old,usuario):
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
  sql=f"UPDATE `billetera` SET `cantidad`={float(cant_act)},`act`=CURRENT_TIMESTAMP WHERE `poseedor`='{usuario}' AND `tipo`='{atc}' AND `billeteraID`='{id1}' "
  sql2=f"UPDATE `billetera` SET `cantidad`={float(cant_old)},`act`=CURRENT_TIMESTAMP WHERE `poseedor`='{usuario}' AND `tipo`='{old}' AND `billeteraID`='{id2}' "
  crs.execute(sql)
  crs.execute(sql2)
  mydb.commit()
  mydb.close()