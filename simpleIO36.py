from quirinoStuff import is_valid, get_user_file
def hapax(string):
    frecuency = {}
    notAcceptedChars = "~!@#$%^&*()_+{}|\":<>?`-=[]\';,./`"
    hapaxWords = []
    words = [i.lower() for i in ("".join([i.lower() for i in string if not i in notAcceptedChars])).split()]
    for word in words:
        if word in frecuency.keys():
            frecuency[word] += 1
        elif word not in frecuency.keys():
            frecuency[word] = 1
    for key in frecuency:
        if frecuency[key] == 1:
            hapaxWords.append(key)
    return hapaxWords

fileName = input("Name of file: ")
while not is_valid(fileName):
    fileName = input("Name of file: ")
myFile = get_user_file(fileName)
print("Hapaxes in", fileName)
for i in hapax(myFile):
    print (i)

tinyStarFields = "\
 　　　　 ˚ 　   ✫   ·　 *   \n\
 ·　　✦ ✦     ✦    ✫        \n\
 　　　　 ˚ 　    ✫  ·　✫ *   \n\
*   　✫ 　　　　✦             \n\
 * 　  　 ✫  · 　 · 　　✫　　  \n\
　　 　 *  ⋆                  \n\
. ˚ 　 *  ✺   🚀　　　✫　  *   \n\
 * 　　　　  *  　　  .✫ 　　 + \n\
. ˚ 　 *  ✺ 　　　✫　  *       \n\
 * 　　　　  *  　　  . 　　 +  \n\
"
print (tinyStarFields)
