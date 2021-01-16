"""

+---------------------------------------+
| In The Name Of God !                  |
+---------------------------------------+
| Project Name : Ashley                 |
| Licence : MIT                         |
| Verson : 0.1.6                        |
|                                       |
| Developer : Amirhossein Mohammsdi     |
| Github    : github.com/BlackIQ/Ashley |
|                                       |
| Last Update : Jan , 17 , 2021         |
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


def do(job):
    c_engine = pyttsx3.init()

    table = "Costume"
    color = "yellow"

    c_engine.say("What site")
    c_engine.runAndWait()
    site = input(colored("What site ? ", color))

    if job == "insert":
        c_engine.say(f"Insert a new {site} account")
        c_engine.runAndWait()
        print(colored(f"Insert a new {site} account . . .\n", color))

        c_engine.say(f"What is your {site} first name")
        c_engine.runAndWait()
        fname = input(colored(f"What is your {site} first name ? ", color))

        c_engine.say(f"What is your {site} last name")
        c_engine.runAndWait()
        lname = input(colored(f"What is your {site} last name ? ", color))

        c_engine.say(f"What is your {site} email")
        c_engine.runAndWait()
        email = input(colored(f"What is your {site} email ? ", color))

        c_engine.say(f"What is your {site} phone")
        c_engine.runAndWait()
        phone = input(colored(f"What is your {site} phone ? ", color))

        c_engine.say(f"What is your {site} username")
        c_engine.runAndWait()
        username = input(colored(f"What is your {site} username ? ", color))

        c_engine.say(f"What is your {site} password")
        c_engine.runAndWait()
        password = getpass(colored(f"What is your {site} password ? ", color))

        if not (fname == None and lname == None and email == None and phone == None and username == None and password == None):
            cursor.execute(
                f"INSERT INTO {table} VALUES ('{fname}' , '{lname}' , '{email}' , '{phone}' , '{username}' , '{password}' , '{site}')")

            cnx.commit()

            c_engine.say("Done")
            c_engine.runAndWait()
            print(colored("\nDone !\n", "yellow"))
        else:
            c_engine.say("Fill all field . Thanks")
            c_engine.runAndWait()
            print("Fill all field . TNX !")

    elif job == "select":
        cursor.execute(f"SELECT * FROM {table} WHERE Site = '{site}'")
        outtable = PrettyTable()
        outtable.field_names = ["First Name", "Last Name", "Email", "Phone", "Username", "Password"]

        for (fname, lname, email, phone, username, password, site) in cursor:
            outtable.add_row([fname, lname, email, phone, username, password])

        print(colored(outtable, "blue"))


def mail(job):
    m_engine = pyttsx3.init()

    table = "Emails"
    color = "yellow"

    m_engine.say("What service")
    m_engine.runAndWait()
    site = input(colored("What service ? ", color))

    if job == "insert":
        m_engine.say(f"Insert a new {site} mail")
        m_engine.runAndWait()
        print(colored(f"Insert a new {site} mail . . .\n", color))

        m_engine.say(f"What is your {site} first name")
        m_engine.runAndWait()
        fname = input(colored(f"What is your {site} first name ? ", color))

        m_engine.say(f"What is your {site} last name")
        m_engine.runAndWait()
        lname = input(colored(f"What is your {site} last name ? ", color))

        m_engine.say(f"What is your {site} phone")
        m_engine.runAndWait()
        phone = input(colored(f"What is your {site} phone ? ", color))

        m_engine.say(f"What is your {site} username")
        m_engine.runAndWait()
        username = input(colored(f"What is your {site} username ? ", color))

        m_engine.say(f"What is your {site} password")
        m_engine.runAndWait()
        password = getpass(colored(f"What is your {site} password ? ", color))

        if not (fname == None and lname == None and phone == None and username == None and password == None):
            cursor.execute(
                f"INSERT INTO {table} VALUES ('{fname}' , '{lname}' , '{username}' , '{password}' , '{phone}' , '{site}')")

            cnx.commit()

            m_engine.say("Done")
            m_engine.runAndWait()
            print(colored("\nDone !\n", color))
        else:
            m_engine.say("Fill all field . Thanks")
            m_engine.runAndWait()
            print("Fill all field . TNX !")

    elif job == "select":
        cursor.execute(f"SELECT * FROM {table} WHERE Site = '{site}'")
        outtable = PrettyTable()
        outtable.field_names = ["First Name", "Last Name", "Username", "Password", "Phone"]

        for (fname, lname, username, password, phone, site) in cursor:
            outtable.add_row([fname, lname, username, password, phone])

        print(colored(outtable, 'magenta'))


def category(which):
    if which == "mail":
        table = "Emails"
        color = "magenta"

        cursor.execute(f"SELECT * FROM {table}")
        outtable = PrettyTable()
        outtable.field_names = ["First Name", "Last Name", "Username", "Password", "Phone", "Service"]

        for (fname, lname, username, password, phone, site) in cursor:
            outtable.add_row([fname, lname, username, password, phone, site])

        print(colored(outtable, color))

    elif which == "site":
        table = "Costume"
        color = "blue"

        cursor.execute(f"SELECT * FROM {table}")
        outtable = PrettyTable()
        outtable.field_names = ["First Name", "Last Name", "Email", "Phone", "Username", "Password", "Site"]

        for (fname, lname, email, phone, username, password, site) in cursor:
            outtable.add_row([fname, lname, email, phone, username, password, site])

        print(colored(outtable, color))
