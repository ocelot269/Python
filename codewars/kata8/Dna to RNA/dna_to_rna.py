def DNAtoRNA(dna):
    RNA = ""
    for letra in dna:
        if letra == "T":
            RNA += "U"
        else:
            RNA += letra
    return RNA

if __name__ == '__main__':

    assert DNAtoRNA("TTTT") == "UUUU"
    assert DNAtoRNA("GCAT") == "GCAU"
    assert DNAtoRNA("GACCGCCGCC") == "GACCGCCGCC"
