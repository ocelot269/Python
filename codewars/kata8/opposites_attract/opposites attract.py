def lovefunc(flower1, flower2):
    if flower1 % 2 != 0 and flower2 % 2 == 0:
        return True
    elif flower1 % 2 == 0 and flower2 % 2 != 0:
        return True
    else:
        return False

if __name__ == '__main__':
    assert lovefunc(1, 4) == True
    assert lovefunc(2, 2) == False
    assert lovefunc(0, 1) == True
    assert lovefunc(0, 0) == False
