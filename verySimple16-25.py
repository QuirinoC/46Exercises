from pprint import pprint

alphabet = {"a":0,"b":0,"c":0,"d":0,"e":0,"f":0,"g":0,"h":0,"i":0,"j":0,\
"k":0,"l":0,"m":0,"n":0,"o":0,"p":0,"q":0,"r":0,"s":0,"t":0,"u":0,"v":0,\
"w":0,"x":0,"y":0,"z":0}
alphaFrecuency = {"a":0,"b":0,"c":0,"d":0,"e":0,"f":0,"g":0,"h":0,"i":0,"j":0,\
"k":0,"l":0,"m":0,"n":0,"o":0,"p":0,"q":0,"r":0,"s":0,"t":0,"u":0,"v":0,\
"w":0,"x":0,"y":0,"z":0}
key = {'a':'n', 'b':'o', 'c':'p', 'd':'q', 'e':'r', 'f':'s', 'g':'t', 'h':'u',
       'i':'v', 'j':'w', 'k':'x', 'l':'y', 'm':'z', 'n':'a', 'o':'b', 'p':'c',
       'q':'d', 'r':'e', 's':'f', 't':'g', 'u':'h', 'v':'i', 'w':'j', 'x':'k',
       'y':'l', 'z':'m', 'A':'N', 'B':'O', 'C':'P', 'D':'Q', 'E':'R', 'F':'S',
       'G':'T', 'H':'U', 'I':'V', 'J':'W', 'K':'X', 'L':'Y', 'M':'Z', 'N':'A',
       'O':'B', 'P':'C', 'Q':'D', 'R':'E', 'S':'F', 'T':'G', 'U':'H', 'V':'I',
       'W':'J', 'X':'K', 'Y':'L', 'Z':'M'}

print (alphaFrecuency)
# 16 filter_long_words
def filter_long_words(list,n):
    newList = []
    for i in list:
        if not len(i) > n:
            newList.append(i)
    return newList

# 17 is_palindrome()

def is_palindrome(string):

    newString = filter(string).lower()
    if newString == newString[::-1]:
        return True
    else:
        return False

def filter(string):
    notAcceptedChars = ['!','$','?','\'','\"',',',".",\
':',';',' ','','','','','','',]
    newstring = ""
    for char in string:
        if not char in notAcceptedChars:
            newstring += char
    return newstring
# 18 is pangram

def is_pangram(string):

    alphaKeys = []
    total = 0

    for key in alphabet.keys():
        alphaKeys.append(key)

    for char in string:
        if char in alphaKeys:
            alphabet[char] += 1

    for key in alphabet:
        if alphabet [key] > 0:
            total += 1

    print (total,len(alphabet.keys()))
    if total == len(alphabet.keys()):
        return True

### 19

# 20 Swedish Translator
def translate(string):
    newString = ""
    swedishDict = \
{"merry":"god", "christmas":"jul", "and":"och", "happy":"gott", \
"new":"nytt", "year":"år"}
    for i in string.split():
        if i.lower() in swedishDict.keys():
            newString += swedishDict[i.lower()] + " "
        else:
            newString += i + " "
    return newString

#21 Frecuency
def char_freq (string):
    print (string)
    for char in string:
        if char in alphaFrecuency.keys():
            alphaFrecuency[char] += 1

    return alphaFrecuency

# 22 Decoder/Encoder
def decoder(string):
    decodedString = ""
    for char in string:
        if char in key.keys():
            decodedString += key[char]
        else:
            decodedString += char
    return decodedString

# 23 correct
def correct(string):
    newString = ""
    for i in string.split():
        newString += i + " "
    return newString

# 24 Third person
def make_3sg_form(string):
    string = string.lower()
    if string.endswith("y"):
        return string[:len(string)-1] + "ies"
    elif string.endswith("o")or\
    string.endswith("o")or\
    string.endswith("ch")or\
    string.endswith("s")or\
    string.endswith("sh")or\
    string.endswith("x")or\
    string.endswith("z"):
        return string + "es"
    else:
        return string + 's'

# 25 Ign form
def make_ing_form(string):
    vowels = ['a','e','i','o','u']
    string = string.lower()
    if string == "be" or string == "see" or string == "flee" or string == "knee":
        return string + "ing"
    elif string.endswith("ie"):
        return string[:len(string)-2] + "ying"
    elif string.endswith("e"):
        return string[:len(string)-1] + "ing"
    elif len(string) == 3 and\
    string [0] not in vowels and string[1] in vowels and string[2] not in vowels:
        return string + string[len(string)-1:len(string)] + "ing"
    else:
        return string + "ing"
########################################
print ("16.")
print (filter_long_words(["Apple","Pen","Pinneapple","Uh"],4),"\n")

print ("17.")
print (is_palindrome("Ana"),"\n")

print ("18.")
print (is_pangram("The quick brown fox jumps over the lazy dog.\n"))


print ("19.")
for i in range(99,0,-1):
    print ("{0} bottles of beer on the wall, {0} bottles of beer.\
\nTake one down, pass it around, {1} bottles of beer on the wall.".format\
(i,i-1),"\n")


print ("20.")
print (translate("Have a merry christmas and a happy new year"),"\n")


print ("21.")
pprint (char_freq("abcabbbababwuidksakjsjksjkskajakjscabcabcabcbacbabcabcabaabaabcbbabcbaccbab"))

print ("22.")
print ("Pnrfne pvcure? V zhpu cersre Pnrfne fnynq!\n",decoder\
("Pnrfne pvcure? V zhpu cersre Pnrfne fnynq!"),"\n")

print ("23.")
print (correct("This   is  very funny  and    cool.Indeed!"),"\n")

print ("24.")
print (make_3sg_form("Try"))
print (make_3sg_form("Bush"))
print (make_3sg_form("Run"))
print (make_3sg_form("Fix"),"\n")

print ("25.")
print (make_ing_form("lie"))
print (make_ing_form("see"))
print (make_ing_form("move"))
print (make_ing_form("hug"))
