# En este ejemplo se borra una BD del servidor 

import mysql.connector

conn1 = mysql.connector.connect(host="localhost",user="root",passwd="")
                               
cur1 = conn1.cursor()

# Borramos la BD y comprobamos

cur1.execute("DROP DATABASE basedepruebas")
cur1.execute("show databases")
print("Esta es la lista de las bases de datos existentes")
num = 0
for base in cur1:
   num = num + 1
   
   print("Elemento ", num, base)
conn1.close()