# En este ejemplo se muestran las bases de datos existentes 

import mysql.connector

# Creamos el nombre de la variable "conn1" 
# y especificamos la conexion con la base de datos
conn1 = mysql.connector.connect(host="localhost",user="root",passwd="")

# Se crea la variable del cursor cur1, que será
# el cursor que se movera por la base de datos
cur1 = conn1.cursor()

# Este comando muestra la lista de las bases de
# datos existentes en el servidor MySQL
cur1.execute("show databases")
print("Esta es la lista de las bases de datos existentes")
num = 0
for base in cur1:
   num = num + 1
   
   print("Elemento ", num, base)
conn1.close()