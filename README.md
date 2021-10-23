# Indice invertido BD

Por:

Miguel Angel Lama Carrasco

Diego Andrey Paredes

Cuenta con 3 programas

## stop_word_cleaner.py
INPUT: no toma input (automaticamente traduce stoplist.txt->stop_words_CLEAN.txt)
traduce las stopwords al vocabulario standard
(no tildes, no ñ, no mayusculas, no caracteres especiales)

## inverted_index.py
INPUT: nombre del archivo (sin formato)
EJEMPLO: libro1
OUTPUT: creará un archivo -inverted-index.txt
Crea el inverted index una simple lista, para su uso eficiente se puede insertar dentro de un diccionario para la lectura
(tiene un limite de 500 palabras)
(esta ordenado en orden alfabetico)

## query.py
INPUT: el query en el formato especificado AND(), AND_NOT(), OR(), L()
EJ:print(AND(L("acaba"),L("afortunadamente")))
OUTPUT: el codigo se ejecuta de manera directa pero en el anterior ejemplo devuelve un set el cual contiene todos los indices con los archivos (y por tanto los archivos)


Notas generales:
Por temas de tiempo algunas de las estructuras son ineficientes especificamente: Stoplist deberia ser un tree para evitar O(n^2), query no deberia ejecutar codigo directo.
si alguien piensa usar este codigo tomar en cuenta que se recomiendan cambios
