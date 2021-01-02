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

# Import Check
import Pack.first as check

check.check()

# Import Py libs
from Pack.status import name as n
from etc.man.man import help
import Pack.core as core

from termcolor import colored
from random import choice
from os import system
import pyttsx3

a_engine = pyttsx3.init()

colors = ['red', 'green', 'white', 'blue', 'cyan', 'magenta', 'grey', 'yellow']
color = choice(colors)

a_engine.say("Welcome")
a_engine.runAndWait()
print(colored("Welcome !\n", color))

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
        print(colored("Bye !", color))
        a_engine.runAndWait()
        core.cnx.close()
        quit()

    elif q == "clear":
        a_engine.say("Clearing the screen")
        a_engine.runAndWait()
        system("clear")

    else:
        a_engine.say("I did not get that !")
        print(colored("I didn't get that !\n", color))
        a_engine.runAndWait()
        pass
