def get_user_file():
    try:

        print("\nFile must be in the same folder, \n\
Please write with extension, if the file is \n\
a .docx please write file.docx\n")
        userInput = input("\nFile name: ")
        # DEBUG
        #userInput = "palindrome.txt"
        file_ = open(userInput,"r+")
        #file_ = open(input("Name of file: \n"),"r+")
        file_string = file_.read()
        file_.close()
    except:
        print ("There is no such file")
        get_user_file(userInput)
    return file_string
def is_palindrome(string):
    '''
        The following line creates a list containing the elements
        in the string excepting a blank space, and then joins it again to the same string
    '''
    string = "".join([i for i in string if (i != " ")])
    if string.lower() == string[::-1].lower():
        return True

def print_palindrome(list):
    for i in list:
        if is_palindrome(i):
            print (i)

userFile = get_user_file()
userFile = userFile.split("\n")

print_palindrome(userFile)
