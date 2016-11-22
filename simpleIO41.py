from random import randint
def lingo():
    print("Welcome to lingo game, guess the fruit")
    words = ["apple","banana","orange","tomato","pear","watermelon",\
"pineapple","cherry"]
    word = words[randint(0,len(words)-1)]
    word = word.lower()
    print ("Hint word has {} characters".format(len(word)))
    userGuess = input("Take a guess\n")
    userGuess = userGuess.lower()

    while userGuess != word:
        hint = ""
        if len(userGuess) <= len(word):
            for i in range(0,len(userGuess)):
                if userGuess[i] == word[i]:
                    hint += "[{}]".format(userGuess[i])
                elif userGuess[i] in word:
                    hint += "({})".format(userGuess[i])
                else:
                    hint += userGuess[i]
            print (hint)
        else:
            print ("Word cant be bigger")
        userGuess = (input().lower())
    print (word, "Correct!")


lingo()
