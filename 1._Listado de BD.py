# En este ejemplo se muestran las bases de datos existentes 

import mysql.connector

# Se crea la conexión con MuySQL con la variable "conn1" 
conn1 = mysql.connector.connect(host="localhost",user="root",passwd="")

# Se crea el cursor para movernos por MySQL con la variable cur1
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