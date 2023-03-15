def word_replacement():
    print("Welcome to the word replacement program!")
    print("This program will replace all instances of a word in a sentence with a new word.")
    print("Please enter a sentence:")
    sentence = input()
    print("Please enter a word to replace:")
    old_word = input()
    print("Please enter a new word:")
    new_word = input()
    new_sentence = sentence.replace(old_word, new_word)
    print("Here is the new sentence:")
    print(new_sentence)
    print("Thank you for using the word replacement program!")

word_replacement()

def reemplazador_palabras():
    """
        Función que reemplaza una palabra por otra en una frase
        Argumentos: Ninguno
        Devuelve: 
        (str): La frase con la palabra reemplazada    
    """
    print('Bienvenido al reemplazador  de palabras')
    print('Por favor ingrese una frase:')
    frase = input()
    print('Por favor ingrese la palabra a reemplazar:')
    palabra = input()
    print('Por favor ingrese la nueva palabra:')
    nueva_palabra = input()
    nueva_frase = frase.replace(palabra, nueva_palabra)
    print('Aquí esta la frase actualizada: ')
    print(nueva_frase)
    print('¡Gracias por usar el reemplazador de palabras!')

reemplazador_palabras()
