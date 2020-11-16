"""

+---------------------------------------+
| In The Name Of God !                  |
+---------------------------------------+
| Project Name : Ashley                 |
| Licence : MIT                         |
| Verson : 0.0.8                        |
|                                       |
| Developer : Amirhossein Mohammsdi     |
| Github : github.com/BlackIQ/Ashley    |
|                                       |
| Last Update : 16 , Nov , 2020         |
+---------------------------------------+

"""

# Import user's data
try:
    from Pack.status import status

    if status == True:
        pass

# If Not
except:
    import os

    print("Ashley database is not set .")
    print("do yo want to install ?")
    ask = input('[y , n] : ')
    if ask == 'y':
        os.system('python3 Pack/init.py')
    else:
        os.system("exit")
    print("ok , done !")
    os.system("clear")

    print("Restart Ashley !")
    quit()

# Import Py libs
import Pack.core as core

# Main loop
while True:
    # Input
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
