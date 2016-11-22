def get_anagrams(string):
    englishWordsFile = open("words.txt","r+")
    englishWords = englishWordsFile.read().split("\n")
    print (len(englishWords))
    values = {"A":1,"B":2,"C":3,"D":4,"E":5,"F":6,"G":7,"H":8,"I":9,\
"J":10,"K":11,"L":12,"M":13,"N":14,"O":15,"P":16,"Q":17,"R":18,"S":19,\
"T":20,"U":21,"V":22,"W":23,"X":24,"Y":25,"Z":26,"'":100,"\"":100,"/":100,\
"1":100,"2":100,"3":100,"4":100,"5":100,"6":100,"7":100,"8":100,"9":100,\
"&":100,"0":100}
    #Gets the value of a string
    stringValue = 0
    for char in string:
        stringValue += values[char.upper()]

    #Returns the user string 'Sorted'
    sortedString = [i for i in string]
    sortedString.sort()

    #Makes a list with the words that have the same lenght of the string
    possibleByLenght = [i for i in englishWords if (len(string) == len(i))]
    possibleByValue = []

    #Makes a shorter list with more possible anagrams giving each letter
    #A Value
    for word in possibleByLenght:
        wordValue = 0
        for char in word:
            wordValue += values[char.upper()]
        if wordValue == stringValue:
            possibleByValue.append(word)

    #Compares if the sorted string and word is the same
    #Since acbdefg and agdbcef sorted are the same (agdbcef),
    #the word should be an
    #Anagram of the string
    anagrams = []
    for word in possibleByValue:
        sortedWord = [i for i in word]
        sortedWord.sort()
        if (sortedWord == sortedString) and (word.lower() != string.lower()):
            anagrams.append(word)

    #Why this didnt work
    '''
        Taking pollo as the string when we would iterate with the for loop
        p is in pirol
        o is in pirol
        l is in pirol
        l is in pirol
        o is in pirol
        pirol

        So it would detect pirol as an anagram of pollo

        I could do something with str.remove() but im not fried
        with that method anymore
    '''
    #Checks if each letter in anagram is in the word
    '''counter = 0
    anagrams = []
    for word in possibleByValue:
        for char in string:
            if char.lower() in word:
                counter += 1
        if (counter == len(word)) and (word != string):
            anagrams.append(word)
        counter = 0'''

    if len(anagrams) > 0:
        return anagrams
    else:
        return "Sorry no anagrams for this one"

print ("Anagram in word finder")
userWord = input("Give me a word (zxz to exit): ")
while userWord != "zxz":
    anagramsInWord = (get_anagrams(userWord))
    if type(anagramsInWord) == str:
        print (anagramsInWord)
    else:
        print ("Anagrams in:",userWord)
        for i in get_anagrams(userWord):
            print (i)
    userWord = input("Give me a word: ")
print ("GoodBye!")
