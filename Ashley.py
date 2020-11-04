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

import mysql.connector

cnx = mysql.connector.connect (
    host='localhost' ,
    user='usr' ,
    password='pswd' ,
    database='Ashley'
)

cursor = cnx.cursor()

print("Welcome !\n\n")


def instagram():
    print("Insert a new Instagram account . . .\n")
    fname = input("What is your first name ? ")
    lname = input("What is your last name ? ")
    email = input("What is your email ? ")
    phone = input("What is your phone ? ")
    username = input("What is your username ? ")
    password = input("What is your password ? ")

    site = 'instagram'

    cursor.execute(f"INSERT INTO Social VALUES ('{fname}' , '{lname}' , '{email}' , '{phone}' , '{username}' , '{password}' , '{site}')")
    cnx.commit()

    print("\nDone !\n")

def twitter():
    print("Insert a new Twitter account . . .\n")
    fname = input("What is your first name ? ")
    lname = input("What is your last name ? ")
    email = input("What is your email ? ")
    phone = input("What is your phone ? ")
    username = input("What is your username ? ")
    password = input("What is your password ? ")

    site = 'twitter'

    cursor.execute(f"INSERT INTO Social VALUES ('{fname}' , '{lname}' , '{email}' , '{phone}' , '{username}' , '{password}' , '{site}')")
    cnx.commit()

    print("\nDone !\n")

def facebook():
    print("Insert a new Facebook account . . .\n")
    fname = input("What is your first name ? ")
    lname = input("What is your last name ? ")
    email = input("What is your email ? ")
    phone = input("What is your phone ? ")
    username = input("What is your username ? ")
    password = input("What is your password ? ")

    site = 'facebook'

    cursor.execute(f"INSERT INTO Social VALUES ('{fname}' , '{lname}' , '{email}' , '{phone}' , '{username}' , '{password}' , '{site}')")
    cnx.commit()

    print("\nDone !\n")

def github():
    print("Insert a new Github account . . .\n")
    fname = input("What is your first name ? ")
    lname = input("What is your last name ? ")
    email = input("What is your email ? ")
    phone = input("What is your phone ? ")
    username = input("What is your username ? ")
    password = input("What is your password ? ")

    site = 'github'

    cursor.execute(f"INSERT INTO Social VALUES ('{fname}' , '{lname}' , '{email}' , '{phone}' , '{username}' , '{password}' , '{site}')")
    cnx.commit()

    print("\nDone !\n")

def show_instagram() :
    site = 'instagram'
    cursor.execute(f"SELECT * FROM Social WHERE Site = '{site}'")
    for (fname , lname , email , phone , username , password , site) in cursor :
        print(f"First name : {fname} | Last name :  {lname} | Phone : {phone} | Email :  {email} | Username : {username} | Password : {password}")

def show_twitter() :
    site = 'twitter'
    cursor.execute(f"SELECT * FROM Social WHERE Site = '{site}'")
    for (fname , lname , email , phone , username , password , site) in cursor :
        print(f"First name : {fname} | Last name :  {lname} | Phone : {phone} | Email :  {email} | Username : {username} | Password : {password}")

def show_facebook() :
    site = 'facebook'
    cursor.execute(f"SELECT * FROM Social WHERE Site = '{site}'")
    for (fname , lname , email , phone , username , password , site) in cursor :
        print(f"First name : {fname} | Last name :  {lname} | Phone : {phone} | Email :  {email} | Username : {username} | Password : {password}")

def show_github() :
    site = 'github'
    cursor.execute(f"SELECT * FROM Social WHERE Site = '{site}'")
    for (fname , lname , email , phone , username , password , site) in cursor :
        print(f"First name : {fname} | Last name :  {lname} | Phone : {phone} | Email :  {email} | Username : {username} | Password : {password}")

while True :
    q = input("What you wanna insert !? ")

    if q == 'instagram' :
        instagram()
    elif q == 'twitter' :
        twitter()
    elif q == 'facebook' :
        facebook()
    elif q == 'github' :
        github()
    elif q == 'show instagram' :
        show_instagram()
    elif q == 'show twitter' :
        show_twitter()
    elif q == 'show facebook' :
        show_facebook()
    elif q == 'show github' :
        show_github()
    elif q == 'List' :
        print('Instagram , Twitter , Facebook , Github')
    else :
        pass

cnx.close()