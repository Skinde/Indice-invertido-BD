import os

def getwordsInFile(fileName):

    array = []
    openFile = open(fileName,"r")
    array = openFile.read().split()
    openFile.close()
    return array

def RemoveProblematicSymbols(array):
    #Made with spanish characters in mind
    for i in range(len(array)):
        word = array[i]

        #UTF-8
        
        #Multiple characters
        word = word.replace("Â«", "")
        word = word.replace("Â»", "")
        word = word.replace("Ã©","e")
        word = word.replace("Ã\xad","i")
        word = word.replace("Ã³","o")
        word = word.replace("Ãº","u")
        word = word.replace("Ã±","n")
        word = word.replace("âº", "")

        #Single characters
        word = word.replace("Ã","a")


        #Simbolos
        word = word.replace(",","")
        word = word.replace(".","")
        word = word.replace(":","")
        word = word.replace(";","")
        word = word.replace("!","")
        word = word.replace("¡","")
        word = word.replace("?","")
        word = word.replace("¿","")
        
        #Spanish characters
        word = word.replace("á","a")
        word = word.replace("é","e")
        word = word.replace("í","i")
        word = word.replace("ó","o")
        word = word.replace("ú","u")
        word = word.replace("ü","u")

        #Lower case
        word = word.lower()

        
        
        array[i] = word
    return array

def clean(filename):
    Openfile = open(filename, "w")
    array = getwordsInFile("stoplist.txt")
    array = RemoveProblematicSymbols(array)
    for word in array:
        Openfile.write(word + "\n")

clean("stop_words_CLEAN.txt")