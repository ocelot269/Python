def getCount(inputStr):
    numVocales = 0
    vocales = {"a", "e", "i", "o", 'u'}
    for vocal in inputStr:
        if vocal in vocales:
            numVocales += 1

    return numVocales

if __name__ == '__main__':

    assert getCount("abracadabra") == 5
