# En este ejemplo se crea una BD en el servidor 

import mysql.connector

conn1 = mysql.connector.connect(host="localhost",user="root",passwd="")
                               
cur1 = conn1.cursor()

# Creamos la BD y comprobamos

cur1.execute("CREATE DATABASE basedepruebas")
cur1.execute("show databases")
for base in cur1:
   print(base)

conn1.close()