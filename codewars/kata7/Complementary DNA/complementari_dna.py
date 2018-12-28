def DNA_strand(dna):
    RNA = {"A": "T", "T": "A", "G": "C", "C": "G", }
    palabra = ""
    for letra in dna:
        if letra in RNA:
            palabra = palabra + RNA[letra]
    return palabra

if __name__ == '__main__':

    assert DNA_strand("AAAA") == "TTTT", "String AAAA is"
    assert DNA_strand("ATTGC") == "TAACG", "String ATTGC is"
    assert DNA_strand("GTAT") == "CATA", "String GTAT is"
