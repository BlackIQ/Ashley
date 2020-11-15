# Import user's data
from .status import *

# Import python libs
import mysql.connector
from prettytable import PrettyTable

# Start the MySQL connector
cnx = mysql.connector.connect(
    host=host,
    user=user,
    password=password,
    database=database
)

# Make a cursor
cursor = cnx.cursor()

print("Welcome !\n\n")


# Instagram Class
class instagram:
    def insert_instagram(self):
        site = 'instagram'
        print("Insert a new Instagram account . . .\n")
        fname = input(f"What is your {site} first name ? ")
        lname = input(f"What is your {site} last name ? ")
        email = input(f"What is your {site} email ? ")
        phone = input(f"What is your {site} phone ? ")
        username = input(f"What is your {site} username ? ")
        password = input(f"What is your {site} password ? ")

        cursor.execute(
            f"INSERT INTO Social VALUES ('{fname}' , '{lname}' , '{email}' , '{phone}' , '{username}' , '{password}' , '{site}')")

        cnx.commit()

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
        site = 'twitter'
        print("Insert a new Twitter account . . .\n")
        fname = input(f"What is your {site} first name ? ")
        lname = input(f"What is your {site} last name ? ")
        email = input(f"What is your {site} email ? ")
        phone = input(f"What is your {site} phone ? ")
        username = input(f"What is your {site} username ? ")
        password = input(f"What is your {site} password ? ")

        cursor.execute(
            f"INSERT INTO Social VALUES ('{fname}' , '{lname}' , '{email}' , '{phone}' , '{username}' , '{password}' , '{site}')")

        cnx.commit()

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
        site = 'facebook'
        print("Insert a new Facebook account . . .\n")
        fname = input(f"What is your {site} first name ? ")
        lname = input(f"What is your {site} last name ? ")
        email = input(f"What is your {site} email ? ")
        phone = input(f"What is your {site} phone ? ")
        username = input(f"What is your {site} username ? ")
        password = input(f"What is your {site} password ? ")

        cursor.execute(
            f"INSERT INTO Social VALUES ('{fname}' , '{lname}' , '{email}' , '{phone}' , '{username}' , '{password}' , '{site}')")

        cnx.commit()

        print("\nDone !\n")

    def show_facebook(self):
        site = 'facebook'
        cursor.execute(f"SELECT * FROM Social WHERE Site = '{site}'")
        facebook_table = PrettyTable()
        facebook_table.field_names = ["First Name", "Last Name", "Email", "Phone", "Username", "Password"]

        for (fname, lname, email, phone, username, password, site) in cursor:
            facebook_table.add_row([fname, lname, email, phone, username, password])

        print(facebook_table)


# Github Class
class github:
    def insert_github(self):
        site = 'github'
        print("Insert a new Github account . . .\n")
        fname = input(f"What is your {site} first name ? ")
        lname = input(f"What is your {site} last name ? ")
        email = input(f"What is your {site} email ? ")
        phone = input(f"What is your {site} phone ? ")
        username = input(f"What is your {site} username ? ")
        password = input(f"What is your {site} password ? ")

        cursor.execute(
            f"INSERT INTO Social VALUES ('{fname}' , '{lname}' , '{email}' , '{phone}' , '{username}' , '{password}' , '{site}')")

        cnx.commit()

        print("\nDone !\n")

    def show_github(self):
        site = 'github'
        cursor.execute(f"SELECT * FROM Social WHERE Site = '{site}'")
        github_table = PrettyTable()
        github_table.field_names = ["First Name", "Last Name", "Email", "Phone", "Username", "Password"]

        for (fname, lname, email, phone, username, password, site) in cursor:
            github_table.add_row([fname, lname, email, phone, username, password])

        print(github_table)


# Stack Over Flow Class
class stack:
    def insert_stack(self):
        site = 'SOF'
        print("Insert a new Stack Over Flow account . . .\n")
        fname = input(f"What is your {site} first name ? ")
        lname = input(f"What is your {site} last name ? ")
        email = input(f"What is your {site} email ? ")
        phone = input(f"What is your {site} phone ? ")
        username = input(f"What is your {site} username ? ")
        password = input(f"What is your {site} password ? ")

        cursor.execute(
            f"INSERT INTO Social VALUES ('{fname}' , '{lname}' , '{email}' , '{phone}' , '{username}' , '{password}' , '{site}')")

        cnx.commit()

        print("\nDone !\n")

    def show_stack(self):
        site = 'SOF'
        cursor.execute(f"SELECT * FROM Social WHERE Site = '{site}'")
        stack_table = PrettyTable()
        stack_table.field_names = ["First Name", "Last Name", "Email", "Phone", "Username", "Password"]

        for (fname, lname, email, phone, username, password, site) in cursor:
            stack_table.add_row([fname, lname, email, phone, username, password])

        print(stack_table)


# Linkedin Class
class linkedin:
    def insert_linkedin(self):
        site = 'linkedin'
        print("Insert a new Linkedin account . . .\n")
        fname = input(f"What is your {site} first name ? ")
        lname = input(f"What is your {site} last name ? ")
        email = input(f"What is your {site} email ? ")
        phone = input(f"What is your {site} phone ? ")
        username = input(f"What is your {site} username ? ")
        password = input(f"What is your {site} password ? ")

        cursor.execute(
            f"INSERT INTO Social VALUES ('{fname}' , '{lname}' , '{email}' , '{phone}' , '{username}' , '{password}' , '{site}')")

        cnx.commit()

        print("\nDone !\n")

    def show_linkedin(self):
        site = 'linkedin'
        cursor.execute(f"SELECT * FROM Social WHERE Site = '{site}'")
        linkedin_table = PrettyTable()
        linkedin_table.field_names = ["First Name", "Last Name", "Email", "Phone", "Username", "Password"]

        for (fname, lname, email, phone, username, password, site) in cursor:
            linkedin_table.add_row([fname, lname, email, phone, username, password])

        print(linkedin_table)


class yahoo:
    def insert_yahoo(self):
        site = 'yahoo'
        print("Insert a new yahoo mail . . .\n")
        fname = input(f"What is your {site} first name ? ")
        lname = input(f"What is your {site} last name ? ")
        username = input(f"What is your {site} username ? ")
        password = input(f"What is your {site} password ? ")
        phone = input(f"What is your {site} phone ? ")

        cursor.execute(
            f"INSERT INTO Emails VALUES ('{fname}' , '{lname}' , '{username}' , '{password}' , '{phone}' , '{site}')")

        cnx.commit()

        print("\nDone !\n")

    def show_yahoo(self):
        site = 'yahoo'
        cursor.execute(f"SELECT * FROM Emails WHERE Site = '{site}'")
        yahoo_table = PrettyTable()
        yahoo_table.field_names = ["First Name", "Last Name", "Username", "Password", "Phone"]

        for (fname, lname, username, password, phone, site) in cursor:
            yahoo_table.add_row([fname, lname, username, password, phone])

        print(yahoo_table)


class gmail:
    def insert_gmail(self):
        site = 'gmail'
        print("Insert a new gmail mail . . .\n")
        fname = input(f"What is your {site} first name ? ")
        lname = input(f"What is your {site} last name ? ")
        username = input(f"What is your {site} username ? ")
        password = input(f"What is your {site} password ? ")
        phone = input(f"What is your {site} phone ? ")

        cursor.execute(
            f"INSERT INTO Emails VALUES ('{fname}' , '{lname}' , '{username}' , '{password}' , '{phone}' , '{site}')")

        cnx.commit()

        print("\nDone !\n")

    def show_gmail(self):
        site = 'gmail'
        cursor.execute(f"SELECT * FROM Emails WHERE Site = '{site}'")
        gmail_table = PrettyTable()
        gmail_table.field_names = ["First Name", "Last Name", "Username", "Password", "Phone"]

        for (fname, lname, username, password, phone, site) in cursor:
            gmail_table.add_row([fname, lname, username, password, phone])

        print(gmail_table)


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

    def all(self):
        print("Social Table :")
        All.social()

        print("\n")

        print("Emails Table :")
        All.emails()

class other:
    def help(self):
        print("Help !")

# Set Social Classes
Instagram = instagram()
Twitter = twitter()
Facebook = facebook()
Github = github()
Stack = stack()
Linkedin = linkedin()

# Set Emails Classes
Yahoo = yahoo()
Gmail = gmail()

# Set All Of Them !
All = all()

# Set Other Class
Other = other()