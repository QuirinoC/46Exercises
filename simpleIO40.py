from random import shuffle, randint
words = ["apple","banana","orange","tomato","pear","watermelon"]
word = words[randint(0,len(words)-1)]
wordList = [i for i in word]
shuffle(wordList)
anagram = "".join(wordList)
print("Fruit word anagram: {}".format(anagram))
print ("Guess the fruit word")
userInput = input()
while userInput != word:
    print ("Guess the fruit word")
    userInput = input()
print ("Correct!")
