try :
    from Pack.status import status
    if status == True :
        pass
except :
    print("Ashley database is not set .")
    print("do yo want to install ?")
    ask = input('[y , n] ')
    if ask == 'y' :
        import os
        os.system('python3 Pack/init.py')
    else :
        import os
        os.system("exit")
    print("ok , done !")
    import os
    os.system("clear")

from Pack.status import *

from time import sleep
import mysql.connector
from prettytable import PrettyTable

cnx = mysql.connector.connect (
    host=host ,
    user=user ,
    password=password ,
    database=database
)

cursor = cnx.cursor()

print("Welcome !\n\n")

class instagram :
    def insert_instagram(self):
        site = 'instagram'
        print("Insert a new Instagram account . . .\n")
        fname = input(f"What is your {site} first name ? ")
        lname = input(f"What is your {site} last name ? ")
        email = input(f"What is your {site} email ? ")
        phone = input(f"What is your {site} phone ? ")
        username = input(f"What is your {site} username ? ")
        password = input(f"What is your {site} password ? ")

        cursor.execute(f"INSERT INTO Social VALUES ('{fname}' , '{lname}' , '{email}' , '{phone}' , '{username}' , '{password}' , '{site}')")

        cnx.commit()

        print("\nDone !\n")

    def show_instagram(self):
        site = 'instagram'
        cursor.execute(f"SELECT * FROM Social WHERE Site = '{site}'")
        instagram_table = PrettyTable()
        instagram_table.field_names = ["First Name", "Last Name", "Email", "Phone", "Username", "Password"]
        for (fname, lname, email, phone, username, password, site) in cursor:
            instagram_table.add_row([fname , lname , email , phone , username , password])
        print(instagram_table)

class twitter :
    def insert_twitter(self):
        site = 'twitter'
        print("Insert a new Twitter account . . .\n")
        fname = input(f"What is your {site} first name ? ")
        lname = input(f"What is your {site} last name ? ")
        email = input(f"What is your {site} email ? ")
        phone = input(f"What is your {site} phone ? ")
        username = input(f"What is your {site} username ? ")
        password = input(f"What is your {site} password ? ")

        cursor.execute(f"INSERT INTO Social VALUES ('{fname}' , '{lname}' , '{email}' , '{phone}' , '{username}' , '{password}' , '{site}')")

        cnx.commit()

        print("\nDone !\n")

    def show_twitter(self) :
        site = 'twitter'
        cursor.execute(f"SELECT * FROM Social WHERE Site = '{site}'")
        twitter_table = PrettyTable()
        twitter_table.field_names = ["First Name", "Last Name", "Email", "Phone", "Username", "Password"]
        for (fname , lname , email , phone , username , password , site) in cursor :
            twitter_table.add_row([fname, lname, email, phone, username, password])
        print(twitter_table)

class facebook :
    def insert_facebook(self):
        site = 'facebook'
        print("Insert a new Facebook account . . .\n")
        fname = input(f"What is your {site} first name ? ")
        lname = input(f"What is your {site} last name ? ")
        email = input(f"What is your {site} email ? ")
        phone = input(f"What is your {site} phone ? ")
        username = input(f"What is your {site} username ? ")
        password = input(f"What is your {site} password ? ")

        cursor.execute(f"INSERT INTO Social VALUES ('{fname}' , '{lname}' , '{email}' , '{phone}' , '{username}' , '{password}' , '{site}')")

        cnx.commit()

        print("\nDone !\n")

    def show_facebook(self) :
        site = 'facebook'
        cursor.execute(f"SELECT * FROM Social WHERE Site = '{site}'")
        facebook_table = PrettyTable()
        facebook_table.field_names = ["First Name", "Last Name", "Email", "Phone", "Username", "Password"]
        for (fname , lname , email , phone , username , password , site) in cursor :
            facebook_table.add_row([fname, lname, email, phone, username, password])
        print(facebook_table)

class github :
    def insert_github(self):
        site = 'github'
        print("Insert a new Github account . . .\n")
        fname = input(f"What is your {site} first name ? ")
        lname = input(f"What is your {site} last name ? ")
        email = input(f"What is your {site} email ? ")
        phone = input(f"What is your {site} phone ? ")
        username = input(f"What is your {site} username ? ")
        password = input(f"What is your {site} password ? ")

        cursor.execute(f"INSERT INTO Social VALUES ('{fname}' , '{lname}' , '{email}' , '{phone}' , '{username}' , '{password}' , '{site}')")

        cnx.commit()

        print("\nDone !\n")

    def show_github(self) :
        site = 'github'
        cursor.execute(f"SELECT * FROM Social WHERE Site = '{site}'")
        github_table = PrettyTable()
        github_table.field_names = ["First Name", "Last Name", "Email", "Phone", "Username", "Password"]
        for (fname , lname , email , phone , username , password , site) in cursor :
            github_table.add_row([fname, lname, email, phone, username, password])
        print(github_table)

class stack :
    def insert_stack(self):
        site = 'SOF'
        print("Insert a new Stack Over Flow account . . .\n")
        fname = input(f"What is your {site} first name ? ")
        lname = input(f"What is your {site} last name ? ")
        email = input(f"What is your {site} email ? ")
        phone = input(f"What is your {site} phone ? ")
        username = input(f"What is your {site} username ? ")
        password = input(f"What is your {site} password ? ")

        cursor.execute(f"INSERT INTO Social VALUES ('{fname}' , '{lname}' , '{email}' , '{phone}' , '{username}' , '{password}' , '{site}')")

        cnx.commit()

        print("\nDone !\n")

    def show_stack(self):
        site = 'SOF'
        cursor.execute(f"SELECT * FROM Social WHERE Site = '{site}'")
        stack_table = PrettyTable()
        stack_table.field_names = ["First Name", "Last Name", "Email", "Phone", "Username", "Password"]
        for (fname, lname, email, phone, username, password, site) in cursor:
            stack_table.add_row([fname , lname , email , phone , username , password])
        print(stack_table)

class linkedin :
    def insert_linkedin(self):
        site = 'linkedin'
        print("Insert a new Linkedin account . . .\n")
        fname = input(f"What is your {site} first name ? ")
        lname = input(f"What is your {site} last name ? ")
        email = input(f"What is your {site} email ? ")
        phone = input(f"What is your {site} phone ? ")
        username = input(f"What is your {site} username ? ")
        password = input(f"What is your {site} password ? ")

        cursor.execute(f"INSERT INTO Social VALUES ('{fname}' , '{lname}' , '{email}' , '{phone}' , '{username}' , '{password}' , '{site}')")

        cnx.commit()

        print("\nDone !\n")

    def show_linkedin(self) :
        site = 'linkedin'
        cursor.execute(f"SELECT * FROM Social WHERE Site = '{site}'")
        linkedin_table = PrettyTable()
        linkedin_table.field_names = ["First Name", "Last Name", "Email", "Phone", "Username", "Password"]
        for (fname , lname , email , phone , username , password , site) in cursor :
            linkedin_table.add_row([fname, lname, email, phone, username, password])
        print(linkedin_table)

Instagram = instagram()
Twitter = twitter()
Facebook = facebook()
Github = github()
Stack = stack()
Linkedin = linkedin()

while True :
    q = input("What you wanna insert !? ")

    if q == 'new instagram' :
        Instagram.insert_instagram()
    elif q == 'new twitter' :
        Twitter.insert_twitter()
    elif q == 'new facebook' :
        Facebook.insert_facebook()
    elif q == 'new github' :
        Github.insert_github()
    elif q == 'new linkedin' :
        Linkedin.insert_linkedin()
    elif q == 'new sof' :
        Stack.insert_stack()

    elif q == 'show instagram' :
        Instagram.show_instagram()
    elif q == 'show twitter' :
        Twitter.show_twitter()
    elif q == 'show facebook' :
        Facebook.show_facebook()
    elif q == 'show github' :
        Github.show_github()
    elif q == 'show linkedin' :
        Linkedin.show_linkedin()
    elif q == 'show sof' :
        Stack.show_stack()

    elif q == 'List' :
        print('Instagram , Twitter , Facebook , Github')
    elif q == 'exit' :
        print("Bye !")
        sleep(3)
        quit()

    else :
        print("I didn't got that !\n")
        pass

cnx.close()