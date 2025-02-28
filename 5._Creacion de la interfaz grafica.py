# En este ejemplo creamos una interfaz basica
import tkinter as tk
import mysql.connector

conn1 = mysql.connector.connect(host="localhost",user="root",passwd="")
                               
cur1 = conn1.cursor()

cur1.execute("show databases")
for base in cur1:
    print(base)
conn1.close()