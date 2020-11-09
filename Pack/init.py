import mysql.connector

print("\n-------------------------------")
print("Welcome to Ashley Init.py !")

host = input("Your MySQL Host ? ")
user = input("Your MySQL User ? ")
password = input("Your MySQL Password ? ")

def w() :
    file = open('Pack/status.py', 'w')
    file.write("status = True\n")
    file.write(f"host = '{host}'\n")
    file.write(f"user = '{user}'\n")
    file.write(f"password = '{password}'\n")
    file.write(f"database = 'Ashley'")
    file.close()

w()

print("Initialising . . .\n")

cnx = mysql.connector.connect (
    host=host ,
    user=user ,
    password=password
)

cursor = cnx.cursor()

print("Executing Queries . . .\n")

cursor.execute('CREATE DATABASE IF NOT EXISTS Ashley')
cursor.execute('USE Ashley')
cursor.execute('CREATE TABLE IF NOT EXISTS `Social` (Fname TEXT , Lname TEXT , Email TEXT , Phone TEXT , Username TEXT , Password TEXT , Site TEXT)')

cnx.close()

print("Writing the file . . .\n")

print("Done !")
print("-------------------------------\n")