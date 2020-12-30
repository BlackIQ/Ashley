"""

+---------------------------------------+
| In The Name Of God !                  |
+---------------------------------------+
| Project Name : Ashley                 |
| Licence : MIT                         |
| Verson : 0.1.2                        |
|                                       |
| Developer : Amirhossein Mohammsdi     |
| Github : github.com/BlackIQ/Ashley    |
|                                       |
| Last Update : 30 , Des , 2020         |
+---------------------------------------+

"""

# Import MySQL
import mysql.connector
from getpass import getpass
import pyttsx3

engine = pyttsx3.init()

print("\n-------------------------------")

engine.say("Welcome to Ashley Init")
print("Welcome to Ashley Init.py !\n")
engine.runAndWait()

# Getting data
engine.say("Your MySQL Host")
engine.runAndWait()
host = input("Your MySQL Host ? ")
engine.say("Your MySQL User")
engine.runAndWait()
user = input("Your MySQL User ? ")
engine.say("Your MySQL Password")
engine.runAndWait()
password = getpass("Your MySQL Password ? ")


# Def Write in file
def w():
    file = open('Pack/status.py', 'w')
    file.write("status = True\n\n")
    file.write(f"host = '{host}'\n")
    file.write(f"user = '{user}'\n")
    file.write(f"password = '{password}'\n")
    file.write(f"database = 'Ashley'")
    file.close()

engine.say("Initialising")
print("\nInitialising . . .\n")
engine.runAndWait()

# Start MySQL Connector
cnx = mysql.connector.connect(
    host=host,
    user=user,
    password=password
)

# Create a cursor
cursor = cnx.cursor()

engine.say("Executing Queries")
print("Executing Queries . . .\n")
engine.runAndWait()

# Executing and creating tables
cursor.execute('CREATE DATABASE IF NOT EXISTS Ashley')
cursor.execute('USE Ashley')

cursor.execute(
    'CREATE TABLE IF NOT EXISTS `Social` (Fname TEXT , Lname TEXT , Email TEXT , Phone TEXT , Username TEXT , Password TEXT , Site TEXT)')
cursor.execute(
    'CREATE TABLE IF NOT EXISTS `Emails` (Fname TEXT , Lname TEXT , Username TEXT , Password TEXT , Phone TEXT , Site TEXT)')
cursor.execute(
    'CREATE TABLE IF NOT EXISTS `Career` (Fname TEXT , Lname TEXT , Email TEXT , Phone TEXT , Username TEXT , Password TEXT , Site TEXT)')

cnx.close()

# Run write in file function
w()

engine.say("Writing in the file")
print("Writing in the file . . .\n")
engine.runAndWait()

engine.say("Done")
print("Done !")
engine.runAndWait()

print("-------------------------------\n")
