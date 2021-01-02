"""

+---------------------------------------+
| In The Name Of God !                  |
+---------------------------------------+
| Project Name : Ashley                 |
| Licence : MIT                         |
| Verson : 0.1.2                        |
|                                       |
| Developer : Amirhossein Mohammsdi     |
| Github : github.com/BlackIQ/Ashley    |
|                                       |
| Last Update : 30 , Des , 2020         |
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
        engine.say("Runnung init")
        print("Running init .")
        engine.runAndWait()
        os.system('python3 Pack/init.py')
        try:
            from Pack.status import status

            if status == True:
                pass
        except:
            engine.say("You entered wrong information")
            print("You entered wrong information .")
            engine.runAndWait()
            quit()
    else:
        quit()
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
from Pack.status import name as n

import pyttsx3
from random import choice
from termcolor import colored

a_engine = pyttsx3.init()

colors = ['red', 'green', 'white', 'blue', 'cyan', 'magenta', 'grey', 'yellow']

# Main loop
while True:
    # Input
    color = choice(colors)

    a_engine.say(f"What you wanna do {n}")
    a_engine.runAndWait()
    q = input(colored(f"What you wanna do {n} ? ", color))

    # Switching !

    # <-----------------------------------------------> #

    # Social ( Insert Part )
    if q == 'new instagram':
        core.do('insert', 'instagram', 'Social')
    elif q == 'new twitter':
        core.do('insert', 'twitter', 'Social')
    elif q == 'new facebook':
        core.do('insert', 'facebook', 'Social')

    # Social ( Show Part )
    elif q == 'show instagram':
        core.do('select', 'instagram', 'Social')
    elif q == 'show twitter':
        core.do('select', 'twitter', 'Social')
    elif q == 'show facebook':
        core.do('select', 'facebook', 'Social')

    # Select Everything in Social
    elif q == "show social":
        core.category('other', 'Social')

    # <-----------------------------------------------> #

    # Career ( Insert Part )
    elif q == 'new github':
        core.do('insert', 'github', 'Career')
    elif q == 'new linkedin':
        core.do('insert', 'linkedin', 'Career')
    elif q == 'new sof':
        core.do('insert', 'stack over flow', 'Career')

    # Career ( Show Part )
    elif q == 'show github':
        core.do('select', 'github', 'Career')
    elif q == 'show linkedin':
        core.do('select', 'linkedin', 'Career')
    elif q == 'show sof':
        core.do('select', 'stack over flow', 'Career')

    # Select Everything in Emails
    elif q == "show career":
        core.category('other', 'Career')

    # <-----------------------------------------------> #

    # Emails ( Insert Part )
    elif q == "new yahoo":
        core.mail('insert', 'yahoo')
    elif q == "new gmail":
        core.mail('insert', 'gmail')

    # Emails ( Show Part )
    elif q == "show yahoo":
        core.mail('select', 'yahoo')
    elif q == "show gmail":
        core.mail('select', 'gmail')

    # Select Everything in Career
    elif q == "show mails":
        core.category('mail', 'Emails')

    # <-----------------------------------------------> #

    # Ashley's Manual
    elif q == 'help':
        a_engine.say("User manual")
        a_engine.runAndWait()
        help()

    # Exit
    elif q == 'exit':
        a_engine.say("Bye !")
        print("Bye !")
        a_engine.runAndWait()
        core.cnx.close()
        quit()

    else:
        a_engine.say("I did not get that !")
        print("I didn't get that !\n")
        a_engine.runAndWait()
        pass
