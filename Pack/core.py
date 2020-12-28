"""

+---------------------------------------+
| In The Name Of God !                  |
+---------------------------------------+
| Project Name : Ashley                 |
| Licence : MIT                         |
| Verson : 0.1.0                        |
|                                       |
| Developer : Amirhossein Mohammsdi     |
| Github : github.com/BlackIQ/Ashley    |
|                                       |
| Last Update : 18 , Nov , 2020         |
+---------------------------------------+

"""

# Import user's data
from .status import *

# Import python libs
from prettytable import PrettyTable
from getpass import getpass
import mysql.connector
import pyttsx3

# Start the MySQL connector
cnx = mysql.connector.connect(
    host=host,
    user=user,
    password=password,
    database=database
)

engine = pyttsx3.init()

# Make a cursor
cursor = cnx.cursor()

engine.say("Welcome")
print("Welcome !\n\n")
engine.runAndWait()


def insert(site, table):
    s_engine = pyttsx3.init()
    s_engine.say(f"Insert a new {site} account")
    print(f"Insert a new {site} account . . .\n")
    s_engine.runAndWait()
    s_engine.say(f"What is your {site} first name")
    s_engine.runAndWait()
    fname = input(f"What is your {site} first name ? ")
    s_engine.say(f"What is your {site} last name")
    s_engine.runAndWait()
    lname = input(f"What is your {site} last name ? ")
    s_engine.say(f"What is your {site} email")
    s_engine.runAndWait()
    email = input(f"What is your {site} email ? ")
    s_engine.say(f"What is your {site} phone")
    s_engine.runAndWait()
    phone = input(f"What is your {site} phone ? ")
    s_engine.say(f"What is your {site} username")
    s_engine.runAndWait()
    username = input(f"What is your {site} username ? ")
    s_engine.say(f"What is your {site} password")
    s_engine.runAndWait()
    password = getpass(f"What is your {site} password ? ")

    cursor.execute(
        f"INSERT INTO {table} VALUES ('{fname}' , '{lname}' , '{email}' , '{phone}' , '{username}' , '{password}' , '{site}')")

    cnx.commit()

    s_engine.say("Done")
    s_engine.runAndWait()
    print("\nDone !\n")


def show(site, table):
    cursor.execute(f"SELECT * FROM {table} WHERE Site = '{site}'")
    outtable = PrettyTable()
    outtable.field_names = ["First Name", "Last Name", "Email", "Phone", "Username", "Password"]

    for (fname, lname, email, phone, username, password, site) in cursor:
        outtable.add_row([fname, lname, email, phone, username, password])

    print(outtable)

def social():
    cursor.execute("SELECT * FROM Social")
    social_table = PrettyTable()
    social_table.field_names = ["First Name", "Last Name", "Email", "Phone", "Username", "Password", "Site"]

    for (fname, lname, email, phone, username, password, site) in cursor:
        social_table.add_row([fname, lname, email, phone, username, password, site])

    print(social_table)

def career():
    cursor.execute("SELECT * FROM Career")
    career_table = PrettyTable()
    career_table.field_names = ["First Name", "Last Name", "Email", "Phone", "Username", "Password", "Site"]

    for (fname, lname, email, phone, username, password, site) in cursor:
        career_table.add_row([fname, lname, email, phone, username, password, site])

    print(career_table)

def emails():
    cursor.execute("SELECT * FROM Emails")
    emails_table = PrettyTable()
    emails_table.field_names = ["First Name", "Last Name", "Username", "Password", "Phone", "Site"]

    for (fname, lname, username, password, phone, site) in cursor:
        emails_table.add_row([fname, lname, username, password, phone, site])

    print(emails_table)

def mail(site, table):
    m_engine = pyttsx3.init()
    m_engine.say(f"Insert a new {site} mail")
    m_engine.runAndWait()
    print(f"Insert a new {site} mail . . .\n")
    m_engine.say(f"what is your {site} first name")
    m_engine.runAndWait()
    fname = input(f"What is your {site} first name ? ")
    m_engine.say(f"what is your {site} last name")
    m_engine.runAndWait()
    lname = input(f"What is your {site} last name ? ")
    m_engine.say(f"what is your {site} username")
    m_engine.runAndWait()
    username = input(f"What is your {site} username ? ")
    m_engine.say(f"what is your {site} password")
    m_engine.runAndWait()
    password = getpass(f"What is your {site} password ? ")
    m_engine.say(f"what is your {site} phone")
    m_engine.runAndWait()
    phone = input(f"What is your {site} phone ? ")

    cursor.execute(
        f"INSERT INTO {table} VALUES ('{fname}' , '{lname}' , '{username}' , '{password}' , '{phone}' , '{site}')")

    cnx.commit()

    m_engine.say("done")
    m_engine.runAndWait()
    print("\nDone !\n")

def show_mail(site):
    cursor.execute(f"SELECT * FROM Emails WHERE Site = '{site}'")
    outtable = PrettyTable()
    outtable.field_names = ["First Name", "Last Name", "Username", "Password", "Phone"]

    for (fname, lname, username, password, phone, site) in cursor:
        outtable.add_row([fname, lname, username, password, phone])

    print(outtable)