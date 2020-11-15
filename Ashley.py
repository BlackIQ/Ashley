# How to see Ashley is set or not

# If yes :
try:
    from Pack.status import status

    if status == True:
        pass

# If Not
except:
    import os

    print("Ashley database is not set .")
    print("do yo want to install ?")
    ask = input('[y , n] ')
    if ask == 'y':
        os.system('python3 Pack/init.py')
    else:
        os.system("exit")
    print("ok , done !")
    os.system("clear")

# Import Py libs
from time import sleep

# Import Ashley core
import Pack.core as core

# Main loop
while True:
    # Input
    q = input("What you wanna insert !? ")

    # Switching !
    if q == 'new instagram':
        core.Instagram.insert_instagram()
    elif q == 'new twitter':
        core.Twitter.insert_twitter()
    elif q == 'new facebook':
        core.Facebook.insert_facebook()
    elif q == 'new github':
        core.Github.insert_github()
    elif q == 'new linkedin':
        core.Linkedin.insert_linkedin()
    elif q == 'new sof':
        core.Stack.insert_stack()

    elif q == 'show instagram':
        core.Instagram.show_instagram()
    elif q == 'show twitter':
        core.Twitter.show_twitter()
    elif q == 'show facebook':
        core.Facebook.show_facebook()
    elif q == 'show github':
        core.Github.show_github()
    elif q == 'show linkedin':
        core.Linkedin.show_linkedin()
    elif q == 'show sof':
        core.Stack.show_stack()

    elif q == "new yahoo":
        core.Yahoo.insert_yahoo()
    elif q == "new gmail":
        core.Gmail.insert_gmail()

    elif q == "show yahoo":
        core.Yahoo.show_yahoo()
    elif q == "show gmail":
        core.Gmail.show_gmail()

    elif q == "show social":
        core.All.social()
    elif q == "show emails":
        core.All.emails()

    elif q == "all":
        core.All.all()

    elif q == 'help':
        core.Other.help()

    elif q == 'exit':
        print("Bye !")
        sleep(2)
        core.cnx.close()
        quit()

    else:
        print("I didn't got that !\n")
        pass
