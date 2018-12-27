def abbrevName(name):
    first, last = name.upper().split(' ')
    return first[0] + "." + last[0]

if __name__ == '__main__':
	
    assert abbrevName("Sam Harris") == "S.H"
    assert abbrevName("Patrick Feenan") == "P.F"
    assert abbrevName("Evan Cole") == "E.C"
    assert abbrevName("P Favuzzi") == "P.F"
    assert abbrevName("David Mendieta") == "D.M"
