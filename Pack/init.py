"""

+---------------------------------------+
| In The Name Of God !                  |
+---------------------------------------+
| Project Name : Ashley                 |
| Licence : MIT                         |
| Verson : 0.1.5                        |
|                                       |
| Developer : Amirhossein Mohammsdi     |
| Github    : github.com/BlackIQ/Ashley |
|                                       |
| Last Update : Jan , 16 , 2021         |
+---------------------------------------+

"""

# Import MySQL
from termcolor import colored
from getpass import getpass
import mysql.connector
import pyttsx3

engine = pyttsx3.init()

print(colored("\n-------------------------------", "red"))

engine.say("Welcome to Ashley Init")
print(colored("Welcome to Ashley Init.py !\n", "cyan"))
engine.runAndWait()

# Getting data
engine.say("Your MySQL Host")
engine.runAndWait()
host = input(colored("Your MySQL Host ? ", "green"))

engine.say("Your MySQL User")
engine.runAndWait()
user = input(colored("Your MySQL User ? ", "green"))

engine.say("Your MySQL Password")
engine.runAndWait()
password = getpass(colored("Your MySQL Password ? ", "green"))

engine.say("Your name")
engine.runAndWait()
name = input(colored("Your Name ? ", "green"))


# Def Write in file
def w():
    file = open('Pack/status.py', 'w')
    file.write("status = True\n\n")
    file.write(f"host = '{host}'\n")
    file.write(f"user = '{user}'\n")
    file.write(f"password = '{password}'\n")
    file.write(f"name = '{name}'\n")
    file.write(f"database = 'Ashley'")
    file.close()


engine.say("Initialising")
print(colored("\nInitialising . . .\n", "cyan"))
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
print(colored("Executing Queries . . .\n", "cyan"))
engine.runAndWait()

# Executing and creating tables
cursor.execute('CREATE DATABASE IF NOT EXISTS Ashley')
cursor.execute('USE Ashley')

cursor.execute(
    'CREATE TABLE IF NOT EXISTS `Emails` (Fname TEXT , Lname TEXT , Username TEXT , Password TEXT , Phone TEXT , Site TEXT)')
cursor.execute(
    'CREATE TABLE IF NOT EXISTS `Costume` (Fname TEXT , Lname TEXT , Email TEXT , Phone TEXT , Username TEXT , Password TEXT , Site TEXT)')

cnx.close()

# Run write in file function
w()

engine.say("Writing in the file")
print(colored("Writing in the file . . .\n", "cyan"))
engine.runAndWait()

engine.say("Done")
print(colored("Done !", "cyan"))
engine.runAndWait()

print(colored("-------------------------------\n", "red"))
