import mysql.connector

def w() :
    file = open('Pack/status.py', 'w')
    file.write("status = True")
    file.close()

print("Initialising . . .\n")

cnx = mysql.connector.connect (
    host='localhost' ,
    user='amir' ,
    password='Black.0481244859IQ.'
)

cursor = cnx.cursor()

print("Executing Queries . . .\n")

cursor.execute('CREATE DATABASE IF NOT EXISTS Ashley')
cursor.execute('USE Ashley')
cursor.execute('CREATE TABLE IF NOT EXISTS `Social` (Fname TEXT , Lname TEXT , Email TEXT , Phone TEXT , Username TEXT , Password TEXT , Site TEXT)')

cnx.close()

print("Writing the file . . .\n")

w()

print("Done !")