# En este ejemplo se cambia la contraseña del servidor 
import mysql.connector

conn1 = mysql.connector.connect(host="localhost",user="root",passwd="")
cur1 = conn1.cursor()

#CAMBIAMOS LA CONTRASEÑA DEL USUARIO
cur1.execute("SET PASSWORD FOR 'root'@'localhost'='1234datos$'")

#ESPERAMOS ACCEDER Y VER EL LISTADO DE BD
conn1 = mysql.connector.connect(host="localhost",user="root",passwd="1234datos$'")
cur1 = conn1.cursor()
cur1.execute("show databases")
print("Esta es la lista de las bases de datos existentes")
num = 0
for base in cur1:
    num = num + 1
    print("Elemento ", num, base)
conn1.close()
