def is_semorndnilap(string):
    string = string.lower()
    reversedString = string.lower()[::-1]
    if reversedString in englishWords:
        return ("{0} {1}".format(string,reversedString))

def getFile(userInput):
    try:
        myFile = open(userInput,"r+")

    except:
        print ("There is no such file")

    return myFile

def start():
    print("Semordnilap Analizer")
    #DEBUG
    ###userInput = "semordnilap.txt"
    #DEBUG
    userInput = input("\nFile name: ")
    userFile = getFile(userInput)
    userList = userFile.read().split("\n")
    for i in userList:
        if is_semorndnilap(i):
            print ("{0} {1}".format(i.lower(),i[::-1].lower()))
    userFile.close()

englishWordsFile = open("words.txt","r+")
englishWords = englishWordsFile.read().split("\n")

start()

englishWordsFile.close()
