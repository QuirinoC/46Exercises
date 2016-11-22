from quirinoStuff import openFile
myFile = openFile()
print ("The average of lenght in a word is %.2f" % \
(len(myFile)/len(myFile.split())))
