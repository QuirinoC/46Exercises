from random import shuffle
def is_balanced(brackets):


    if brackets[0] == "]":
        return False

    list = []
    for bracket in brackets:
        if bracket == '[':
            list.append(0)
        elif bracket == ']' and len(list) == 0:
            return False
        elif bracket == ']':
            list.pop()
    if len(list) == 0:
        return True
    else:
        return False

def create_brackets(n):
    brackets = []
    for i in range(n):
        brackets.append('[')
        brackets.append(']')
    shuffle(brackets)
    bracketString = "".join(brackets)
    return bracketString

def valid_userInput(userInput):

    try:
        userInput = int(userInput)
    except:
        print ("Invalid Number")
        return False
    return True

print ("Number of opening/closing is the half of elements the \
list will have, number of strings is the number of bracket sets \
the program will create\n")

print ("Number of opening/closing brackets:")
nBrackets = input("N: ")
while not valid_userInput(nBrackets):
    nBrackets = input("N: ")
nBrackets = int(nBrackets)



print ("Number of strings: ")
nStrings = input("N: ")
while not valid_userInput(nStrings):
    nStrings = input("N: ")
nStrings = int(nStrings)

for i in range(nStrings):
    brackets = create_brackets(nBrackets)
    if is_balanced(brackets):
        print (brackets, "OK")
    else:
        print (brackets, "NOT OK")
