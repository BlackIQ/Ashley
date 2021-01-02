def check():
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