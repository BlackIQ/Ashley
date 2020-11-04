'''
try :
    from Pack.var.status import status
    if status == True :
        pass
except :
    print("Ashley database is not set .")
    print("do yo want to install ?")
    ask = input('[y , n] ')
    if ask == 'y' :
        import os
        os.system('python3 Pack/Ashley/src/init.py')
    else :
        import os
        os.system("exit")
    print("ok , done !")
    import os
    os.system("clear")
'''

import mysql.connector
cnx = mysql.connector.connect(
    host='localhost' ,
    user='amir' ,
    password='Black.0481244859IQ.' ,
    database='Ashley'
)

print("Welcome !")

print("Insert a new Instagram account\n")
fname = input("What is your first name ? ")
lname = input("What is your last name ? ")
email = input("What is your email ? ")
phone = input("What is your phone ? ")
username = input("What is your username ? ")
password = input("What is your password ? ")

site = 'instagram'

cursor = cnx.cursor()
cursor.execute(f"INSERT INTO Social VALUES ('{fname}' , '{lname}' , '{email}' , '{phone}' , '{username}' , '{password}' , '{site}')")
cnx.commit()

cnx.close()