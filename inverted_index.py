import os
import random

dictionary = {}


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
        word = word.replace("Ã\xad","i")
        word = word.replace("Â«","")
        word = word.replace("Â»","")
        word = word.replace("Ã‰","E")
        word = word.replace("Ã©","e")
        word = word.replace("Ã³","o")
        word = word.replace("Ãº","u")
        word = word.replace("Ã±","n")
        word = word.replace("Ãš","u")
        word = word.replace("Âº","")
        word = word.replace("Ã¢","a")
        

        #Single characters
        word = word.replace("Ã","a")
        word = word.replace("»","u")
        word = word.replace("â","")
        

        #Simbolos
        word = word.replace(",","")
        word = word.replace(".","")
        word = word.replace(":","")
        word = word.replace(";","")
        word = word.replace("!","")
        word = word.replace("¡","")
        word = word.replace("?","")
        word = word.replace("¿","")
        word = word.replace("º","")
        word = word.replace("(","")
        word = word.replace(")","")
        word = word.replace("{","")
        word = word.replace("}","")
        word = word.replace("[","")
        word = word.replace("]","")
        word = word.replace("\"","")
        word = word.replace("\\","")
        

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


def remove_stop_words(array):
    bad_array = getwordsInFile("stop_words_CLEAN.txt")
    output_array = [[0 for x in range(0)] for y in range(0)] 
    for element in array:
        if element not in bad_array:
            output_array.append(element)
    return output_array


def createInvertedIndex(array, filename):
    requires_removal = False
    for i in range(len(array)):
        word = array[i]
        if word in dictionary:
                if filename not in dictionary[word]:
                    dictionary[word] = dictionary[word] + "," + filename
        else:
            dictionary[word] = ":" + filename


#Randomly removes elements untill you have 500     
def deleteExcess(requires_removal):
    random_factor = 0
    size_removal = len(dictionary) - 500
    while requires_removal:
        if size_removal == 0:
            requires_removal = False
            break
        if random_factor > 100:
            size_removal = size_removal + 1
            random_factor = 0
        key = random.choice(list(dictionary.keys()))
        if len(dictionary[key].split(',')) <= size_removal:
            del dictionary[key]
            size_removal = size_removal - 1
        else:
            random_factor = random_factor + 1

def write_dictionary(filename):
    Openfile = open(filename, "w")
    for key in sorted(dictionary):
        value = dictionary[key]
        Openfile.write(key + value + "\n")
        



size = 0
for document in ["libro1.txt", "libro2.txt", "libro3.txt", "libro4.txt", "libro5.txt", "libro6.txt"]:
    array = getwordsInFile(document)
    array = RemoveProblematicSymbols(array)
    array = remove_stop_words(array)
    size = createInvertedIndex(array, document)
    print(array)
if len(dictionary) > 500:
    deleteExcess(True)
write_dictionary("inverted-index.dat")

        
        
