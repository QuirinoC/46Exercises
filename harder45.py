from random import shuffle
from math import floor
pokemons = "audino \
bagon baltoy banette bidoof braviary bronzor \
carracosta charmeleon cresselia croagunk \
darmanitan deino emboar \
emolga exeggcute \
gabite girafarig gulpin \
haxorus heatmor heatran \
ivysaur \
jellicent jumpluff \
kangaskhan kricketune \
landorus ledyba loudred lumineon lunatone \
machamp magnezone mamoswine \
nosepass \
petilil pidgeotto pikachu pinsir poliwrath poochyena porygon2 porygonz \
registeel relicanth remoraid rufflet \
sableye scolipede scrafty seaking sealeo silcoon simisear snivy snorlax spoink starly \
tirtouga trapinch treecko tyrogue \
vigoroth vulpix \
wailord wartortle whismur wingull \
yamask"\
.split()

def chain(word,elements,wordChain):
    #print (word)
    elements = newList(elements)
    wordChain.append(word)
    elements.remove(word)
    for nextWord in elements:
        #print (word[-1] == nextWord[0])
        if word[-1] == nextWord[0]:
            chain(nextWord,elements,wordChain)
            return wordChain
    newWordChain = newList(wordChain)
    wordChain = []
    return newWordChain

def newList(list):
    anotherList = []
    for i in list:
        anotherList.append(i)
    return anotherList

def biggerList(setLists):
    biggest = 0

    for indexOfList in range(0,len(setLists)):
        if len(setLists[indexOfList]) > len(setLists[biggest]):
            biggest = indexOfList
    return setLists[biggest]
print ("Time (in seconds) you want to give the program to run \
(more is better)")
print ("Note: Time depends on computer specs")
time = int(floor(float(input("Time: \n"))/4))*1000
print ("This might take a while...")


finalChain = []

for i in range(time):
    shuffle(pokemons)
    setOfChains = []
    for pokemon in pokemons:
        setOfChains.append(chain(pokemon,pokemons,[]))
    finalChain.append(biggerList(setOfChains))

    #print ("{}/{}".format(i,n))
print ("The biggest (maybe) possible combination of \
pokemons that generates the longest chain is {} with {} pokemons"\
.format(biggerList(finalChain),len(biggerList(finalChain))))
