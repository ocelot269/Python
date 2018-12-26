def bool_to_word(boolean):
    if boolean:
        return "Yes"
    return "No"

if __name__ == '__main__':

    assert bool_to_word(True) == 'Yes'
    assert bool_to_word(False) == 'No'
