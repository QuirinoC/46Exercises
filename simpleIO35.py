import os
from time import sleep
d = {'a':'alpha', 'b':'bravo', 'c':'charlie', 'd':'delta', 'e':'echo', 'f':'foxtrot',
     'g':'golf', 'h':'hotel', 'i':'india', 'j':'juliett', 'k':'kilo', 'l':'lima',
     'm':'mike', 'n':'november', 'o':'oscar', 'p':'papa', 'q':'quebec', 'r':'romeo',
     's':'sierra', 't':'tango', 'u':'uniform', 'v':'victor', 'w':'whiskey',
     'x':'x-ray', 'y':'yankee', 'z':'zulu'}

def speak_ICAO(message,timeICAO,timeWord):
    for i in message:
        if i == " ":
            sleep(timeWord)
        if i.lower() in d:
            os.system("say "+ d[i.lower()])
            sleep(timeICAO)


print("Sorry only OS X")
speak_ICAO(input("Message... "),0.1,0.7)
