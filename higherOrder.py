from functools import reduce
#30
#31
def map(function,list):
    newList = []
    for i in list:
        newList.append(function(i))
    return newList
def filter(function,list):
    newList = []
    for i in list:
        if function(i):
            newList.append(i)
    return newList
def reduce(function,iterable,initializer = None):
    iterable = iter(iterable)
    if initializer == None:
        value = next(iterable)
    else:
        value = initializer

    for i in iterable:
        value = function(value,i)
    return value

# 26 reduce()
def max_in_list(list):
    return reduce (lambda x,y: x if (x > y) else y,list)

# 27 map a list of words
# 27-1
def lenWords1(list):
    newList = []
    for i in list:
        newList.append(len(i))
    return newList
# 27-2
def lenWords2(list):
    newList = []
    l = lambda x: len(x)
    for i in map(l,list):
        newList.append(i)
    return newList
# 27-3
def lenWords3(list):
    newList = []
    newList = ([len(x) for x in list])
    return newList

# 28
def find_longest_word(list):
    a = lambda x: len(x)
    lenList = map(a,list)
    return reduce (lambda x,y: x if (x > y) else y,lenList)

# 29
def filter_long_words(list, n):
    newList = []
    for i in filter(lambda x: (len(x) >= n), list):
        newList.append(i)
    return newList

# 30 Use the map to translate
swedishDict = \
{"merry":"god", "christmas":"jul", "and":"och", "happy":"gott", \
"new":"nytt", "year":"år"}
def translate(string):
    list = [i.lower() for i in string.split()]
    translated = map(lambda x: swedishDict[x] if (x in swedishDict) else x,list)
    translatedList = [i for i in translated]
    newString = ""
    for i in translatedList:
        newString += i + " "
    return newString.capitalize()

# 31 Is on top
'''
--------------------------------------------------------------
'''
print ("\n These are higher order")
# 26
print  (max_in_list([5,12,4,52,6,2,7]))

# 27-1
print (lenWords1(["Hello","World","!"]))
# 27-2
print (lenWords2(["Goodbye","World","!"]))
# 27-3
print (lenWords3(["Hello","Wall","!"]))

# 28
print (find_longest_word(["Juan","Carlos","Quirino","Carrasco___","Juanito"]))

# 29
print (filter_long_words(["Hola","amigo","como", "te", "va?","heuheuheu","doggo",""],5))

# 30
print (translate("Have a merry christmas and a happy new year"))
