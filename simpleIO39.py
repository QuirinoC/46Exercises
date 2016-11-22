from random import randint
def guess_the_number():
    print ("Hello! Whats your name? ")
    userName = input()
    print("Well, {}, I am thinking of a number between 1 and 20".format(userName.capitalize()))
    number = randint(1,20)
    print (number)
    print ("Take a guess")
    userGuess = int(input())
    counter = 1
    while userGuess != number:
        if userGuess < number:
            print ("Your guess is too low")
            print ("Take a guess")
            userGuess = int(input())
        else:
            print ("Your guess is to high")
            print ("Take a guess")
            userGuess = int(input())
        counter += 1
    print ("Good job, {0}! You guessed my number in {1} guesses".format(userName,counter))
guess_the_number()
