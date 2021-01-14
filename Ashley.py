"""

+---------------------------------------+
| In The Name Of God !                  |
+---------------------------------------+
| Project Name : Ashley                 |
| Licence : MIT                         |
| Verson : 0.1.4                        |
|                                       |
| Developer : Amirhossein Mohammsdi     |
| Github    : github.com/BlackIQ/Ashley |
|                                       |
| Last Update : 12 , Jan , 2021         |
+---------------------------------------+

"""

# Import Check
import Pack.first as check

check.clear()
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

colors = ['red', 'green', 'white', 'blue', 'cyan', 'magenta', 'yellow']
color = choice(colors)

system("clear")

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

    # Costume ( Insert Part )
    if q == "new":
        core.costume("insert")

    # Emails ( Show Part )
    elif q == "show":
        core.costume("select")

    elif q == "show costume -A":
        core.costume("all")

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

    # Select Everything in Emails
    elif q == "show mails":
        core.mail('all', None)

    # <-----------------------------------------------> #

    # Ashley's Manual
    elif q == 'help':
        a_engine.say("User manual")
        a_engine.runAndWait()
        help()

    # Exit
    elif q == 'exit':
        a_engine.say("Bye")
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
