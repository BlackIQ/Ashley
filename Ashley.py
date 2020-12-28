"""

+---------------------------------------+
| In The Name Of God !                  |
+---------------------------------------+
| Project Name : Ashley                 |
| Licence : MIT                         |
| Verson : 0.1.1                        |
|                                       |
| Developer : Amirhossein Mohammsdi     |
| Github : github.com/BlackIQ/Ashley    |
|                                       |
| Last Update : 28 , Des , 2020         |
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
from etc.man.man import help
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
        core.insert('instagram', 'Social')
    elif q == 'new twitter':
        core.insert('twitter', 'Social')
    elif q == 'new facebook':
        core.insert('facebook', 'Social')

    # Social ( Show Part )
    elif q == 'show instagram':
        core.show('instagram', 'Social')
    elif q == 'show twitter':
        core.show('twitter', 'Social')
    elif q == 'show facebook':
        core.show('facebook', 'Social')

    # Select Everything in Social
    elif q == "show social":
        core.social()

    # <-----------------------------------------------> #

    # Career ( Insert Part )
    elif q == 'new github':
        core.insert('github', 'Career')
    elif q == 'new linkedin':
        core.insert('linkedin', 'Career')
    elif q == 'new sof':
        core.insert('Stack Over Flow', 'Career')

    # Career ( Show Part )
    elif q == 'show github':
        core.show('github', 'Career')
    elif q == 'show linkedin':
        core.show('linkedin', 'Career')
    elif q == 'show sof':
        core.show('Stack Over Flow', 'Career')

    # Select Everything in Emails
    elif q == "show career":
        core.career()

    # <-----------------------------------------------> #

    # Emails ( Insert Part )
    elif q == "new yahoo":
        core.mail('yahoo', 'Emails')
    elif q == "new gmail":
        core.mail('gmail', 'Emails')

    # Emails ( Show Part )
    elif q == "show yahoo":
        core.show_mail('yahoo')
    elif q == "show gmail":
        core.show_mail('gmail')

    # Select Everything in Career
    elif q == "show mails":
        core.emails()

    # <-----------------------------------------------> #

    # Ashley's Manual
    elif q == 'help':
        help()

    # Exit
    elif q == 'exit':
        print("Bye !")
        core.cnx.close()
        quit()

    else:
        print("I didn't get that !\n")
        pass
