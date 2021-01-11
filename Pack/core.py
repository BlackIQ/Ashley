"""

+---------------------------------------+
| In The Name Of God !                  |
+---------------------------------------+
| Project Name : Ashley                 |
| Licence : MIT                         |
| Verson : 0.1.3                        |
|                                       |
| Developer : Amirhossein Mohammsdi     |
| Github : github.com/BlackIQ/Ashley    |
|                                       |
| Last Update : 2 , Jan , 2021          |
+---------------------------------------+

"""

# Import user's data
from .status import *

# Import python libs
from prettytable import PrettyTable
from getpass import getpass
import mysql.connector
import pyttsx3
from termcolor import colored

# Start the MySQL connector
cnx = mysql.connector.connect(
    host=host,
    user=user,
    password=password,
    database=database
)

# Make a cursor
cursor = cnx.cursor()

def do(job, site, table):
    if job == "insert":
        s_engine = pyttsx3.init()

        s_engine.say(f"Insert a new {site} account")
        s_engine.runAndWait()
        print(colored(f"Insert a new {site} account . . .\n", 'yellow'))

        s_engine.say(f"What is your {site} first name")
        s_engine.runAndWait()
        fname = input(colored(f"What is your {site} first name ? ", "yellow"))

        s_engine.say(f"What is your {site} last name")
        s_engine.runAndWait()
        lname = input(colored(f"What is your {site} last name ? ", "yellow"))

        s_engine.say(f"What is your {site} email")
        s_engine.runAndWait()
        email = input(colored(f"What is your {site} email ? ", "yellow"))

        s_engine.say(f"What is your {site} phone")
        s_engine.runAndWait()
        phone = input(colored(f"What is your {site} phone ? ", "yellow"))

        s_engine.say(f"What is your {site} username")
        s_engine.runAndWait()
        username = input(colored(f"What is your {site} username ? ", "yellow"))

        s_engine.say(f"What is your {site} password")
        s_engine.runAndWait()
        password = getpass(colored(f"What is your {site} password ? ", "yellow"))

        cursor.execute(
            f"INSERT INTO {table} VALUES ('{fname}' , '{lname}' , '{email}' , '{phone}' , '{username}' , '{password}' , '{site}')")

        cnx.commit()

        s_engine.say("Done")
        s_engine.runAndWait()
        print(colored("\nDone !\n", "yellow"))

    elif job == "select":
        cursor.execute(f"SELECT * FROM {table} WHERE Site = '{site}'")
        outtable = PrettyTable()
        outtable.field_names = ["First Name", "Last Name", "Email", "Phone", "Username", "Password"]

        for (fname, lname, email, phone, username, password, site) in cursor:
            outtable.add_row([fname, lname, email, phone, username, password])

        if table == "Social":
            print(colored(outtable, 'blue'))
        elif table == "Career":
            print(colored(outtable, 'green'))
        else:
            pass


def category(what, table):
    if what == "other":
        cursor.execute(f"SELECT * FROM {table}")
        outtable = PrettyTable()
        outtable.field_names = ["First Name", "Last Name", "Email", "Phone", "Username", "Password", "Site"]

        for (fname, lname, email, phone, username, password, site) in cursor:
            outtable.add_row([fname, lname, email, phone, username, password, site])

        if table == "Social":
            print(colored(outtable, 'blue'))
        elif table == "Career":
            print(colored(outtable, 'green'))
        else:
            pass


def mail(job, site):
    if job == "insert":
        m_engine = pyttsx3.init()

        m_engine.say(f"Insert a new {site} mail")
        m_engine.runAndWait()
        print(colored(f"Insert a new {site} mail . . .\n", "yellow"))

        m_engine.say(f"What is your {site} first name")
        m_engine.runAndWait()
        fname = input(colored(f"What is your {site} first name ? ", "yellow"))

        m_engine.say(f"What is your {site} last name")
        m_engine.runAndWait()
        lname = input(colored(f"What is your {site} last name ? ", "yellow"))

        m_engine.say(f"What is your {site} phone")
        m_engine.runAndWait()
        phone = input(colored(f"What is your {site} phone ? ", "yellow"))

        m_engine.say(f"What is your {site} username")
        m_engine.runAndWait()
        username = input(colored(f"What is your {site} username ? ", "yellow"))

        m_engine.say(f"What is your {site} password")
        m_engine.runAndWait()
        password = getpass(colored(f"What is your {site} password ? ", "yellow"))

        cursor.execute(
            f"INSERT INTO Emails VALUES ('{fname}' , '{lname}' , '{username}' , '{password}' , '{phone}' , '{site}')")

        cnx.commit()

        m_engine.say("Done")
        m_engine.runAndWait()
        print(colored("\nDone !\n", "yellow"))

    elif job == "select":
        cursor.execute(f"SELECT * FROM Emails WHERE Site = '{site}'")
        outtable = PrettyTable()
        outtable.field_names = ["First Name", "Last Name", "Username", "Password", "Phone"]

        for (fname, lname, username, password, phone, site) in cursor:
            outtable.add_row([fname, lname, username, password, phone])

        print(colored(outtable, 'magenta'))
