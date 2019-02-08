import uuid
import pyperclip
import webbrowser

usehooks = 0

webbrowser.open('https://registrace.seznam.cz/?service=email&return_url=https%3A%2F%2Femail.seznam.cz%2F')

while True:
    rand = str(uuid.uuid4())
    input("Press enter for random username")
    pyperclip.copy(str(rand[:8]))
    print (str(rand[:8]) + " " + "Has been copied to clipboard")
    input("Press enter for random password")
    pyperclip.copy(str(rand))
    print (str(rand) + " " + "Has been copied to clipboard")
    input("Press enter for year of birth")
    print ("1990 Has been copied to clipboard")
    pyperclip.copy("1990")
    file = open("emails.txt","a")
    file.write(str(rand[:8]) + "@seznam.cz" + ":" + str(rand)+ '\n')
    file.close()
    if usehooks == 1:
        from dhooks import Webhook
        hook = Webhook('WEBHOOK_HERE_IF_ENABLED')
        hook.send("```New Seznam account```")
        hook.send("```" + str(rand[:8]) + "@seznam.cz" + ":" + str(rand) + "```")
    input("Press enter when you are ready to create another account")

    
        
    
