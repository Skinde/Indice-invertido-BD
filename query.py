import os

def getIndex(fileName):
    file = open(fileName, "r")
    lines = file.readlines()
    output = {}
    for line in lines:
        line = line.replace("\n","")
        array = line.split(',')
        for things in array:
            if not things == array[0]:
                output[array[0]] = things
    return output

        

def L(word):
    locations = set()
    for filex in os.listdir(os.getcwd()):
        if filex.endswith("-inverted-array.dat"):
            index = getIndex(filex)
            if word in index:
                locations.add(filex)
    return locations
            
    return False
def AND(locations1, locations2):
    return set.intersection(locations1, locations2)

def OR(locations1, locations2):
    return set.union(locations1, locations2)

def AND_NOT(locations1, locations2):
    locations1 = locations1 - locations2
    return locations1

#WARNING this is retarded
inp = input()
start_changing = False
sanitized_input = ""
for i in range(len(inp)):
    word = inp[i]
    if start_changing:

        word = word.replace("á","a")
        word = word.replace("é","e")
        word = word.replace("í","i")
        word = word.replace("ó","o")
        word = word.replace("ú","u")
        word = word.replace("ü","u")
        word = word.lower()
        
    if word == "\"":
        if start_changing:
            start_changing = False
        else:
            start_changing = True
    sanitized_input = sanitized_input + word
exec(sanitized_input)



