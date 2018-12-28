def solution(str):
    return str[::-1]

if __name__ == '__main__':

    assert solution('world') == 'dlrow'
    assert solution('hello') == 'olleh'
    assert solution('') == ''
    assert solution('h') == 'h'
