def remove_char(s):
    menos = s[1:-1]
    return menos

if __name__ == '__main__':

    assert remove_char('eloquent') == 'loquen'
    assert remove_char('country') == 'ountr'
    assert remove_char('person') == 'erso'
    assert remove_char('place') == 'lac'
    assert remove_char('ok') == ''
