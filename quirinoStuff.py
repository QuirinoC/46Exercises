def get_user_file(userInput):
    '''
        Returns a file as a string given the name of the file
    '''
    file_ = open(userInput,"r+")
    file_string = file_.read()
    file_.close()
    return file_string

def is_valid(nameOfFile):
    '''
        Makes sure the file itself exist
    '''
    print("\nFile must be in the same folder, \n\
Please write with extension, if the file is \n\
a .docx please write file.docx\n")
    try:
        aFile = open(nameOfFile,"r+")
        aFile.close()
        return True
    except:
        print("There is no such file")
def openFile():
    '''
        get_user_file and is_valid
    '''
    fileName = input("Name of File: ")
    while not is_valid(fileName):
        fileName = input("Name of File: ")
    return get_user_file(fileName)
