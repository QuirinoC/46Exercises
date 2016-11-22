# 1 max() function
def max(a,b):
    if a > b:
        return a
    elif b > a:
        return b

# 2 max_of_three function
def max_of_three(a,b,c):
    myList = []
    myList.append(a)
    myList.append(b)
    myList.append(c)
    myList.sort()
    return myList[len(myList)-1]

# 3 length of string/list
def length(thing):
    counter = 0
    for i in thing:
        counter += 1
    return counter

# 4 True if vowel, false if
def isVowel(char):
    if char.lower() in vowels:
        return True
    else:
        return False

# 5 rövarspråket Translator
def swedish_translate(string):
    translated = ""
    for i in string:
        if i.lower() not in vowels:
            translated += i + "o" + i
        else:
            translated += i
    return translated.capitalize()

# 6 Sum() and multiply()
def sum(sumList):
    result = 0
    for i in sumList:
        result += i
    return result

def multiply(multiplyList):
    result = 1
    for i in multiplyList:
        result *= i
    return result

# 7 Reversal of string
def reverse(string):
    return string[::-1]
vowels = ["a","e","i","o","u"] #This is used in #4 and #5

# 8 is_palindrome()
def is_palindrome(string):
    if string.lower() == string[::-1].lower():
        return True

# 9 is_member()
def is_member(x,list):
    for i in list:
        if x == i:
            return True
    return False

# 10 overlapping()
def overlapping(list0,list1):
    for x in list0:
        for y in list1:
            if x == y:
                return True
    return False

# 11 generate_n_chars()
def generate_n_chars(n,c):
    string = ""
    for i in range(0,n):
        string += c
    return string
    pass

# 12 Histogram
def histogram(list):
    for i in list:
        print(i * "*")

# 13 Max of list
def max_in_list(list):
    list.sort()
    return list[len(list)-1]

# 14 length in words
def length_of_words(list):
    lenWords = []
    for i in list:
        lenWords.append(len(i))
    return lenWords
'''
_______________________________________________________________________________

                                                                            '''
# 1
print("1.")
print ("{0} is the biggest number\n".format(max(100,101)))

# 2
print ("2.")
print ("{0} is the biggest number\n".format(max_of_three(164,143,201000)))

# 3
print ("3.")
print ("This string has {0} elements".format(length("Hello Boy")))
print ("This list has {0} elements\n".format(length([1,54,3,63,23,64,3])))

# 4
charForExcercise4 = "B"
print("4.")
print ("Its {0} that \"{1}\" is a vowel\n".format\
(isVowel(charForExcercise4),charForExcercise4))

# 5
stringForExcercise5 = "Otorrinolaringologo"
print ("5.")
print ("{0} in rövarspråket is {1}\n".format\
(stringForExcercise5,swedish_translate(stringForExcercise5)))

# 6
sumListForExcercise6 = [1,2,3,4]
multiplyListForExcercise6 = [1,2,3,4]
print("6.")
print ("The sum of {0} is {1}".format\
(sumListForExcercise6,sum(sumListForExcercise6)))
print ("The multiplication of {0} is {1}\n".\
format(multiplyListForExcercise6,multiply(multiplyListForExcercise6)))

# 7
stringForExcercise7 = "Good bye"
print ("7.")
print ("{0} reversed is:\n{1}\n".format\
(stringForExcercise7,reverse(stringForExcercise7)))

# 8
print ("8.")
if (is_palindrome("sanas")):
    print ("Sanas is a word palindrome")
print ()

print ("9.")
print ("Is {0} that {1} is in {2}".format\
(is_member(5,[1,2,3,4,5]),5,[1,2,3,4,5]))
print()

print ("10.")
print ([1,2,3,4],[532,34,12,1,356],overlapping([1,2,3,4],[532,34,12,1,356]))
print ()

print ("11.")
print (generate_n_chars(10,'z'))
print ()

print ("12.")
histogram([5,1,25,6])
print ()

print ("13.")
print ([1,2,4,6,3,5,6,3,6,8,54,643,443,4,21,14,23,121],max_in_list\
([1,2,4,6,3,5,6,3,6,8,54,643,443,4,21,14,23,121]))
print()

print ("14.")
print (["Hola","Como","Te","Va"],length_of_words(["Hola","Como","Te","Va"]))
print ()

print ("15.")
print (["Apple", "Banana", "Juan", "Trash", "Car"], max_in_list(length_of_words\
(["Apple", "Banana", "Juan", "Trash", "Car"])))
print ()
