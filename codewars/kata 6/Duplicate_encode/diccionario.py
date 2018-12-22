def duplicate_encode(palabra):
    encoded = {}
    palabra = palabra.lower()
    for letra in palabra:
        if letra not in encoded:
            encoded[letra] = "("

        elif letra in encoded:
            encoded[letra] = ")"
    contador = ""
    for letra in palabra:
        contador = contador + encoded[letra]
        
    return contador

if __name__ == '__main__':

        # Casos test

    assert(duplicate_encode("din"))
    #>>>"((("
    assert(duplicate_encode("recede"))
    #>>> "()()()"
    assert(duplicate_encode("Success"))
    #>>>")())())", "should ignore case"
    assert(duplicate_encode("(( @"))
    #>>>"))(("
