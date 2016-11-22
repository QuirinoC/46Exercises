def get_user_file(userInput):
    file_ = open(userInput,"r+")
    file_string = file_.read()
    file_.close()
    return file_string

def is_valid(nameOfFile):
    try:
        aFile = open(nameOfFile,"r+")
        aFile.close()
        return True
    except:
        print("There is no such file")

def char_freq_table(string,fileName):
    frecuency = {}
    chars = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q",\
    "R","S","T","U","V","W","X","Y","Z"]
    for i in string:
        if (i.upper() in chars) and (not i.upper() in frecuency.keys()):
            frecuency[i.upper()] = 1
        elif (i.upper() in chars) and ( i.upper() in frecuency.keys()):
            frecuency[i.upper()] += 1

    print ("Char frecuency in {}".format(fileName))
    for i in chars:
        if i in frecuency.keys():
            print ("{} : {}".format(i,frecuency[i]))

    return frecuency



def start():

    print("\nFile must be in the same folder, \n\
Please write with extension, if the file is \n\
a .docx please write file.docx\n")

    fileName = "poem.txt"
    fileName = input("File Name: ")
    while not is_valid(fileName):
        fileName = input("File Name: ")

    userFile = get_user_file(fileName)

    char_freq_table(userFile,fileName)

start()
