from quirinoStuff import openFile
userFile = openFile()
counter = 1
for i in userFile.split("\n"):
    print (counter, "|", i)
    counter += 1
