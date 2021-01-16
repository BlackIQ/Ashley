"""

+---------------------------------------+
| In The Name Of God !                  |
+---------------------------------------+
| Project Name : Ashley                 |
| Licence : MIT                         |
| Verson : 0.1.5                        |
|                                       |
| Developer : Amirhossein Mohammsdi     |
| Github    : github.com/BlackIQ/Ashley |
|                                       |
| Last Update : 16 , Jan , 2021         |
+---------------------------------------+

"""

from termcolor import colored
import pyttsx3
import os

def clear():
    os.system("clear")

def check():
    # Import user's data
    try:
        from Pack.status import status

        if status == True:
            pass

    # If Not
    except:
        engine = pyttsx3.init()

        engine.say("Ashley database is not set")
        print(colored("Ashley database is not set .", "magenta"))
        engine.runAndWait()
        engine.say("do yo want to install")
        print(colored("do yo want to install ?", "magenta"))
        engine.runAndWait()
        ask = input(colored('[y , n] : ', "yellow"))
        if ask == 'y':
            engine.say("Runnung init")
            print(colored("\nRunning init .", "blue"))
            engine.runAndWait()
            os.system('python3 Pack/init.py')
            try:
                from Pack.status import status

                if status == True:
                    pass
            except:
                engine.say("You entered wrong information")
                print(colored("You entered wrong information .", "red"))
                engine.runAndWait()
                quit()
        else:
            quit()
        engine.say("ok , done")
        print(colored("ok , done !", "green"))
        engine.runAndWait()

        engine.say("Please restart Ashley")
        print(colored("Please restart Ashley !", "magenta"))
        engine.runAndWait()

        quit()