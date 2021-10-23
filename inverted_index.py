import os
import random

def getwordsInFile(fileName):

    array = []
    openFile = open(fileName,"r")
    array = openFile.read().split()
    openFile.close()
    return array

def position_atacher(array):
    internal_array = []
    external_array = [[0 for x in range(0)] for y in range(0)] 
    character_count = 0
    for i in range(len(array)):
        internal_array = [array[i], str(i)]
        external_array.append(internal_array)
    return external_array

def RemoveProblematicSymbols(array):
    #Made with spanish characters in mind
    for i in range(len(array)):
        word = array[i][0]

        #UTF-8
        
        #Multiple characters
        word = word.replace("Ã\xad","i")
        word = word.replace("Â«","")
        word = word.replace("Â»","")
        word = word.replace("Ã©","e")
        word = word.replace("Ã³","o")
        word = word.replace("Ãº","u")
        word = word.replace("Ã±","n")
        word = word.replace("Ãš","u")
        word = word.replace("Âº","")
        

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

        
        
        array[i][0] = word
    return array


def remove_stop_words(array):
    bad_array = getwordsInFile("stop_words_CLEAN.txt")
    output_array = [[0 for x in range(0)] for y in range(0)] 
    for element in array:
        if element[0] not in bad_array:
            output_array.append(element)
    return output_array

def createInvertedIndex(array, filename):
    Openfile = open(filename, "w")
    dictionary = {}
    requires_removal = False
    size = 0 
    for i in range(len(array)):
        word = array[i][0]
        if word in dictionary:
            dictionary[word] = dictionary[word] + "," + array[i][1]
        else:
            dictionary[word] = "," + array[i][1]
        if i > 500:
            requires_removal = True
        size = size + 1

    #Randomly removes elements untill you have 500
    random_factor = 0
    size_removal = size - 500
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
        

    for key in sorted(dictionary):
        value = dictionary[key]
        Openfile.write(key + value + "\n")
        



filename = input()
array = getwordsInFile(filename + ".txt")
new_array = position_atacher(array)
new_array = RemoveProblematicSymbols(new_array)
new_array = remove_stop_words(new_array)
print(new_array)
createInvertedIndex(new_array, filename + "-inverted-array.dat")

        
        
