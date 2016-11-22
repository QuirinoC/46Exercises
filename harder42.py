def splitter(string):
    #The indexes of the periods
    titles = "\
Dr. Esq. Hon. Jr. Mr. Mrs. Ms. Messrs. \
Mmes. Msgr. Prof. Rev. Rt. Hon. Sr. St.\
"
    titles = titles.split()
    #😬
    #Replace the period in a title for the emoji
    for title in titles:
        if title in string:
            string = string.replace(title,title[0:len(title)-1] + "😬")
    periods = get_periods(string)

    listed = [i for i in string]

    periods = get_periods("".join(listed))

    #If the following char is something
    for i in periods:
        if (listed[i+1] != " "):
            listed[i] = "😬"

    periods = get_periods("".join(listed))

    for i in periods:
        if (listed[i] == listed[i-1]) or (listed[i-1] == "😬"):
            listed[i] = "😬"

    periods = get_periods("".join(listed))

    for i in periods:
        if (listed[i+1] == " ") and (listed[i+2] == listed[i+2].lower()):
            listed[i] = "😬"

    periods = get_periods("".join(listed))

    lines = "".join(listed).split(".")

    newString = ""
    if "".join(lines)[len(lines)-1] == ".":
        lines = lines[0:len(lines)-1]

    for line in lines:
        if line[0:1] == " ":
            newString += (line[1:len(line)])
            newString += ".\n"
        else:
            newString += line
            newString += ".\n"
    newString = newString.replace("😬",".")
    return newString

def get_periods(string):
    #Get the indexes of the periods in the list
    periods = []
    for i in range(0,len(string)):
        if string[i] == "." and (i != 0) and (i != len(string)-1):
            periods.append(i)
    return periods

string = \
"Your task here is to write a program that given the name of a text file is able to write its content with each sentence on a separate line. Test your program with the following short text: Mr. Smith bought cheapsite.com for 1.5 million dollars, i.e. he paid a lot for it. Did he mind? Adam Jones Jr. thinks he didn't. In any case, this isn't true... Well, with a probability of .9 it isn't. The result should be:"
print (string,'\n')
print (splitter(string))

'''

'''
