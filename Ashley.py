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

from time import sleep

import Pack.core as core

while True :
    q = input("What you wanna insert !? ")

    if q == 'new instagram' :
        core.Instagram.insert_instagram()
    elif q == 'new twitter' :
        core.Twitter.insert_twitter()
    elif q == 'new facebook' :
        core.Facebook.insert_facebook()
    elif q == 'new github' :
        core.Github.insert_github()
    elif q == 'new linkedin' :
        core.Linkedin.insert_linkedin()
    elif q == 'new sof' :
        core.Stack.insert_stack()

    elif q == 'show instagram' :
        core.Instagram.show_instagram()
    elif q == 'show twitter' :
        core.Twitter.show_twitter()
    elif q == 'show facebook' :
        core.Facebook.show_facebook()
    elif q == 'show github' :
        core.Github.show_github()
    elif q == 'show linkedin' :
        core.Linkedin.show_linkedin()
    elif q == 'show sof' :
        core.Stack.show_stack()

    elif q == 'List' :
        print('Instagram , Twitter , Facebook , Github , Stack Over Flow , Linkedin')

    elif q == 'exit' :
        print("Bye !")
        sleep(3)
        core.cnx.close()
        quit()

    else :
        print("I didn't got that !\n")
        pass