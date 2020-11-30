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
try:
    from Pack.status import status

    if status == True:
        pass

# If Not
except:
    import pyttsx3
    import os

    engine = pyttsx3.init()

    engine.say("Ashley database is not set")
    print("Ashley database is not set .")
    engine.runAndWait()
    engine.say("do yo want to install")
    print("do yo want to install ?")
    engine.runAndWait()
    ask = input('[y , n] : ')
    if ask == 'y':
        os.system('python3 Pack/init.py')
    else:
        os.system("exit")
    engine.say("ok , done")
    print("ok , done !")
    engine.runAndWait()
    os.system("clear")

    engine.say("Restart Ashley")
    print("Restart Ashley !")
    engine.runAndWait()

    quit()

# Import Py libs
import Pack.core as core

import pyttsx3

a_engine = pyttsx3.init()

# Main loop
while True:
    # Input
    a_engine.say("What you wanna insert")
    a_engine.runAndWait()
    q = input("What you wanna insert !? ")

    # Switching !

    # Social ( Insert Part )
    if q == 'new instagram':
        core.Social.Instagram.insert_instagram()
    elif q == 'new twitter':
        core.Social.Twitter.insert_twitter()
    elif q == 'new facebook':
        core.Social.Facebook.insert_facebook()

    # Career ( Insert Part )
    elif q == 'new github':
        core.Career.Github.insert_github()
    elif q == 'new linkedin':
        core.Career.Linkedin.insert_linkedin()
    elif q == 'new sof':
        core.Career.Stack.insert_stack()

    # Emails ( Insert Part )
    elif q == "new yahoo":
        core.Email.Yahoo.insert_yahoo()
    elif q == "new gmail":
        core.Email.Gmail.insert_gmail()

    # Social ( Show Part )
    elif q == 'show instagram':
        core.Social.Instagram.show_instagram()
    elif q == 'show twitter':
        core.Social.Twitter.show_twitter()
    elif q == 'show facebook':
        core.Social.Facebook.show_facebook()

    # Career ( Show Part )
    elif q == 'show github':
        core.Career.Github.show_github()
    elif q == 'show linkedin':
        core.Career.Linkedin.show_linkedin()
    elif q == 'show sof':
        core.Career.Stack.show_stack()

    # Emails ( Show Part )
    elif q == "show yahoo":
        core.Email.Yahoo.show_yahoo()
    elif q == "show gmail":
        core.Email.Gmail.show_gmail()

    # Select Everything in Social
    elif q == "show social":
        core.All.social()
    # Select Everything in Emails
    elif q == "show emails":
        core.All.emails()
    # Select Everything in Career
    elif q == "show career":
        core.All.career()

    # Select Everything in Database
    elif q == "all":
        core.All.all()

    # Ashley's Manual
    elif q == 'help':
        from etc.man.man import help

        help()

    # Exit
    elif q == 'exit':
        print("Bye !")
        core.cnx.close()
        quit()

    else:
        print("I didn't get that !\n")
        pass
