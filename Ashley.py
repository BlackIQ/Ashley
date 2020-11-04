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

import Pack.core as core

import mysql.connector

cnx = mysql.connector.connect(
    host='localhost' ,
    user='user' ,
    password='pswd' ,
    database='Ashley'
)

cursor = cnx.cursor()

print("Welcome !")

while True :
    q = input("What to do !? ")

    if q == 'instagram' :
        core.get_instagram()
    else :
        pass


def instagram(fname , lname , email , phone , username , password , site) :
    cursor.execute(f"INSERT INTO Social VALUES ('{fname}' , '{lname}' , '{email}' , '{phone}' , '{username}' , '{password}' , '{site}')")
    cnx.commit()

cnx.close()