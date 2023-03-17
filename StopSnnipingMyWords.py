
'''Stop gninnipS My sdroW!
Write a function that takes in a string of one or more words, 
and returns the same string, but with all five or more letter words reversed 
(Just like the name of this Kata). Strings passed in will consist of only 
letters and spaces. 
Spaces will be included only when more than one word is present.

Examples:
spinWords( "Hey fellow warriors" ) => returns "Hey wollef sroirraw" 
spinWords( "This is a test") => returns "This is a test" 
spinWords( "This is another test" )=> returns "This is rehtona test"
'''

def spin_words(cadena):
    palabras = cadena.split()
    for i in range(len(palabras)):
        if len(palabras[i]) > 4:
            palabras[i] = palabras[i][::-1]
    return " ".join(palabras)

def test_sentences():
    # Test 1: Palabras de longitud menor a 5 no se invierten
    assert spin_words("Hola Mundo") == "Hola odnuM"
    
    # Test 2: Palabras de longitud mayor o igual a 5 se invierten
    assert spin_words("Este es un ejemplo") == "Este es un olpmeje"
    
    # Test 3: Cadena vacía
    assert spin_words("") == ""
    
    # Test 4: Una sola palabra de longitud mayor o igual a 5 se invierte
    assert spin_words("Python") == "nohtyP"
    
    # Test 5: Todas las palabras de longitud mayor o igual a 5 se invierten
    assert spin_words("Aprender Python es divertido") == "rednerpA nohtyP es oditrevid"
    
    print("Todos los casos de prueba han pasado")

test_sentences()    