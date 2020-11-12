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


# Set Classes
Instagram = instagram()
Twitter = twitter()
Facebook = facebook()
Github = github()
Stack = stack()
Linkedin = linkedin()