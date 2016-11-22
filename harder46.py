from time import sleep
from quirinoStuff import get_user_file
englishWords = get_user_file("words.txt").split()

def getWords(string,words):
    wordOne = ""
    wordTwo = ""
    even = [i for i in range(len(string)) if (i % 2 == 0)]
    odd = [i for i in range(len(string)) if (i % 2 != 0)]
    for i in even:
        wordOne += string[i]
    for i in odd:
        wordTwo += string[i]
    if (wordOne in words) and (wordTwo in words):
        return ("\"{}\": makes \"{}\" and \"{}\"".format(string,wordOne,wordTwo))
    return None

alternades = open("alternades.txt","w")

print ("This program will create an alternate.txt")
print ("In the same folder as the python script")
print ("Program will start in 10 seconds")
sleep(10)
for word in englishWords:
    alternade = getWords(word,englishWords)
    if alternade != None:
        print (alternade)
        alternades.write("{}\n".format(alternade))
alternades.close()
