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


class social:
    # Instagram Class
    class instagram:
        def insert_instagram(self):
            s_engine = pyttsx3.init()
            site = 'instagram'
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
                f"INSERT INTO Social VALUES ('{fname}' , '{lname}' , '{email}' , '{phone}' , '{username}' , '{password}' , '{site}')")

            cnx.commit()

            s_engine.say("Done")
            s_engine.runAndWait()
            print("\nDone !\n")

        def show_instagram(self):
            site = 'instagram'
            cursor.execute(f"SELECT * FROM Social WHERE Site = '{site}'")
            instagram_table = PrettyTable()
            instagram_table.field_names = ["First Name", "Last Name", "Email", "Phone", "Username", "Password"]

            for (fname, lname, email, phone, username, password, site) in cursor:
                instagram_table.add_row([fname, lname, email, phone, username, password])

            print(instagram_table)

    # Twitter Class
    class twitter:
        def insert_twitter(self):
            s_engine = pyttsx3.init()
            site = 'twitter'
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
                f"INSERT INTO Social VALUES ('{fname}' , '{lname}' , '{email}' , '{phone}' , '{username}' , '{password}' , '{site}')")

            cnx.commit()

            s_engine.say("Done")
            s_engine.runAndWait()
            print("\nDone !\n")

        def show_twitter(self):
            site = 'twitter'
            cursor.execute(f"SELECT * FROM Social WHERE Site = '{site}'")
            twitter_table = PrettyTable()
            twitter_table.field_names = ["First Name", "Last Name", "Email", "Phone", "Username", "Password"]

            for (fname, lname, email, phone, username, password, site) in cursor:
                twitter_table.add_row([fname, lname, email, phone, username, password])

            print(twitter_table)

    # Facebook Class
    class facebook:
        def insert_facebook(self):
            s_engine = pyttsx3.init()
            site = 'facebook'
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
                f"INSERT INTO Social VALUES ('{fname}' , '{lname}' , '{email}' , '{phone}' , '{username}' , '{password}' , '{site}')")

            cnx.commit()

            s_engine.say("Done")
            s_engine.runAndWait()
            print("\nDone !\n")

        def show_facebook(self):
            site = 'facebook'
            cursor.execute(f"SELECT * FROM Social WHERE Site = '{site}'")
            facebook_table = PrettyTable()
            facebook_table.field_names = ["First Name", "Last Name", "Email", "Phone", "Username", "Password"]

            for (fname, lname, email, phone, username, password, site) in cursor:
                facebook_table.add_row([fname, lname, email, phone, username, password])

            print(facebook_table)

    Instagram = instagram()
    Twitter = twitter()
    Facebook = facebook()


class career:
    # Github Class
    class github:
        def insert_github(self):
            c_engine = pyttsx3.init()
            site = 'github'
            c_engine.say(f"Insert a new {site} account")
            print(f"Insert a new {site} account . . .\n")
            c_engine.runAndWait()
            c_engine.say(f"What is your {site} first name")
            c_engine.runAndWait()
            fname = input(f"What is your {site} first name ? ")
            c_engine.say(f"What is your {site} last name")
            c_engine.runAndWait()
            lname = input(f"What is your {site} last name ? ")
            c_engine.say(f"What is your {site} email")
            c_engine.runAndWait()
            email = input(f"What is your {site} email ? ")
            c_engine.say(f"What is your {site} phone")
            c_engine.runAndWait()
            phone = input(f"What is your {site} phone ? ")
            c_engine.say(f"What is your {site} username")
            c_engine.runAndWait()
            username = input(f"What is your {site} username ? ")
            c_engine.say(f"What is your {site} password")
            c_engine.runAndWait()
            password = getpass(f"What is your {site} password ? ")

            cursor.execute(
                f"INSERT INTO Career VALUES ('{fname}' , '{lname}' , '{email}' , '{phone}' , '{username}' , '{password}' , '{site}')")

            cnx.commit()

            c_engine.say("Done")
            c_engine.runAndWait()
            print("\nDone !\n")

        def show_github(self):
            site = 'github'
            cursor.execute(f"SELECT * FROM Career WHERE Site = '{site}'")
            github_table = PrettyTable()
            github_table.field_names = ["First Name", "Last Name", "Email", "Phone", "Username", "Password"]

            for (fname, lname, email, phone, username, password, site) in cursor:
                github_table.add_row([fname, lname, email, phone, username, password])

            print(github_table)

    # Stack Over Flow Class
    class stack:
        def insert_stack(self):
            c_engine = pyttsx3.init()
            site = 'Stack Over Flow'
            c_engine.say(f"Insert a new {site} account")
            print(f"Insert a new {site} account . . .\n")
            c_engine.runAndWait()
            c_engine.say(f"What is your {site} first name")
            c_engine.runAndWait()
            fname = input(f"What is your {site} first name ? ")
            c_engine.say(f"What is your {site} last name")
            c_engine.runAndWait()
            lname = input(f"What is your {site} last name ? ")
            c_engine.say(f"What is your {site} email")
            c_engine.runAndWait()
            email = input(f"What is your {site} email ? ")
            c_engine.say(f"What is your {site} phone")
            c_engine.runAndWait()
            phone = input(f"What is your {site} phone ? ")
            c_engine.say(f"What is your {site} username")
            c_engine.runAndWait()
            username = input(f"What is your {site} username ? ")
            c_engine.say(f"What is your {site} password")
            c_engine.runAndWait()
            password = getpass(f"What is your {site} password ? ")

            cursor.execute(
                f"INSERT INTO Career VALUES ('{fname}' , '{lname}' , '{email}' , '{phone}' , '{username}' , '{password}' , '{site}')")

            cnx.commit()

            c_engine.say("Done")
            c_engine.runAndWait()
            print("\nDone !\n")

        def show_stack(self):
            site = 'Stack Over Flow'
            cursor.execute(f"SELECT * FROM Career WHERE Site = '{site}'")
            stack_table = PrettyTable()
            stack_table.field_names = ["First Name", "Last Name", "Email", "Phone", "Username", "Password"]

            for (fname, lname, email, phone, username, password, site) in cursor:
                stack_table.add_row([fname, lname, email, phone, username, password])

            print(stack_table)

    # Linkedin Class
    class linkedin:
        def insert_linkedin(self):
            c_engine = pyttsx3.init()
            site = 'linkedin'
            c_engine.say(f"Insert a new {site} account")
            print(f"Insert a new {site} account . . .\n")
            c_engine.runAndWait()
            c_engine.say(f"What is your {site} first name")
            c_engine.runAndWait()
            fname = input(f"What is your {site} first name ? ")
            c_engine.say(f"What is your {site} last name")
            c_engine.runAndWait()
            lname = input(f"What is your {site} last name ? ")
            c_engine.say(f"What is your {site} email")
            c_engine.runAndWait()
            email = input(f"What is your {site} email ? ")
            c_engine.say(f"What is your {site} phone")
            c_engine.runAndWait()
            phone = input(f"What is your {site} phone ? ")
            c_engine.say(f"What is your {site} username")
            c_engine.runAndWait()
            username = input(f"What is your {site} username ? ")
            c_engine.say(f"What is your {site} password")
            c_engine.runAndWait()
            password = getpass(f"What is your {site} password ? ")

            cursor.execute(
                f"INSERT INTO Career VALUES ('{fname}' , '{lname}' , '{email}' , '{phone}' , '{username}' , '{password}' , '{site}')")

            cnx.commit()

            c_engine.say("Done")
            c_engine.runAndWait()
            print("\nDone !\n")

        def show_linkedin(self):
            site = 'linkedin'
            cursor.execute(f"SELECT * FROM Career WHERE Site = '{site}'")
            linkedin_table = PrettyTable()
            linkedin_table.field_names = ["First Name", "Last Name", "Email", "Phone", "Username", "Password"]

            for (fname, lname, email, phone, username, password, site) in cursor:
                linkedin_table.add_row([fname, lname, email, phone, username, password])

            print(linkedin_table)

    # Set Social Classes
    Github = github()
    Stack = stack()
    Linkedin = linkedin()


class mail:
    # Yahoo Class
    class yahoo:
        def insert_yahoo(self):
            m_engine = pyttsx3.init()
            site = 'yahoo'
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
                f"INSERT INTO Emails VALUES ('{fname}' , '{lname}' , '{username}' , '{password}' , '{phone}' , '{site}')")

            cnx.commit()

            m_engine.say("done")
            m_engine.runAndWait()
            print("\nDone !\n")

        def show_yahoo(self):
            site = 'yahoo'
            cursor.execute(f"SELECT * FROM Emails WHERE Site = '{site}'")
            yahoo_table = PrettyTable()
            yahoo_table.field_names = ["First Name", "Last Name", "Username", "Password", "Phone"]

            for (fname, lname, username, password, phone, site) in cursor:
                yahoo_table.add_row([fname, lname, username, password, phone])

            print(yahoo_table)

    # Class Gmail
    class gmail:
        def insert_gmail(self):
            m_engine = pyttsx3.init()
            site = 'gmail'
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
                f"INSERT INTO Emails VALUES ('{fname}' , '{lname}' , '{username}' , '{password}' , '{phone}' , '{site}')")

            cnx.commit()

            m_engine.say("done")
            m_engine.runAndWait()
            print("\nDone !\n")

        def show_gmail(self):
            site = 'gmail'
            cursor.execute(f"SELECT * FROM Emails WHERE Site = '{site}'")
            gmail_table = PrettyTable()
            gmail_table.field_names = ["First Name", "Last Name", "Username", "Password", "Phone"]

            for (fname, lname, username, password, phone, site) in cursor:
                gmail_table.add_row([fname, lname, username, password, phone])

            print(gmail_table)

    # Set Emails Classes
    Yahoo = yahoo()
    Gmail = gmail()


class all:
    def social(self):
        cursor.execute("SELECT * FROM Social")
        social_table = PrettyTable()
        social_table.field_names = ["First Name", "Last Name", "Email", "Phone", "Username", "Password", "Site"]

        for (fname, lname, email, phone, username, password, site) in cursor:
            social_table.add_row([fname, lname, email, phone, username, password, site])

        print(social_table)

    def emails(self):
        cursor.execute("SELECT * FROM Emails")
        emails_table = PrettyTable()
        emails_table.field_names = ["First Name", "Last Name", "Username", "Password", "Phone", "Site"]

        for (fname, lname, username, password, phone, site) in cursor:
            emails_table.add_row([fname, lname, username, password, phone, site])

        print(emails_table)

    def career(self):
        cursor.execute("SELECT * FROM Career")
        career_table = PrettyTable()
        career_table.field_names = ["First Name", "Last Name", "Email", "Phone", "Username", "Password", "Site"]

        for (fname, lname, email, phone, username, password, site) in cursor:
            career_table.add_row([fname, lname, email, phone, username, password, site])

        print(career_table)

    def all(self):
        print("Social Table :")
        All.social()

        print("\n")

        print("Careers Table :")
        All.career()

        print("\n")

        print("Emails Table :")
        All.emails()


# Set All Of Them !
All = all()

# Main Classes
Social = social()
Career = career()
Email = mail()
