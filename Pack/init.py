"""

+---------------------------------------+
| In The Name Of God !                  |
+---------------------------------------+
| Project Name : Ashley                 |
| Licence : MIT                         |
| Verson : 0.0.7                        |
|                                       |
| Developer : Amirhossein Mohammsdi     |
| Github : github.com/BlackIQ/Ashley    |
|                                       |
| Last Update : 15 , Nov , 2020         |
+---------------------------------------+

"""

# Import MySQL
import mysql.connector
from getpass import getpass

print("\n-------------------------------")
print("Welcome to Ashley Init.py !")

# Getting data
host = input("Your MySQL Host ? ")
user = input("Your MySQL User ? ")
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


# Run write in file function
w()

print("\nInitialising . . .\n")

# Start MySQL Connector
cnx = mysql.connector.connect(
    host=host,
    user=user,
    password=password
)

# Create a cursor
cursor = cnx.cursor()

print("Executing Queries . . .\n")

# Executing and creating tables
cursor.execute('CREATE DATABASE IF NOT EXISTS Ashley')
cursor.execute('USE Ashley')
cursor.execute(
    'CREATE TABLE IF NOT EXISTS `Social` (Fname TEXT , Lname TEXT , Email TEXT , Phone TEXT , Username TEXT , Password TEXT , Site TEXT)')
cursor.execute(
    'CREATE TABLE IF NOT EXISTS `Emails` (Fname TEXT , Lname TEXT , Username TEXT , Password TEXT , Phone TEXT , Site TEXT)')

cnx.close()

print("Writing the file . . .\n")

print("Done !")
print("-------------------------------\n")
