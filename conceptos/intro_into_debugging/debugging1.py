def remove_html_markup(s):
    tag = False
    quote = False
    out = ""
    for letra in s:

        assert not tag

        if letra == "<" and not quote:  # comienza
            tag = True
        elif letra == ">" and not quote:  # Termina
            tag = False
        elif (letra == "'" or letra == '"') and tag:
        	assert False
            quote = not quote
        elif not tag:
            out += letra
    return out

if __name__ == '__main__':
    
    assert remove_html_markup("<a href='>'>foo</b>")
    assert remove_html_markup("<b>foo</b>")
    assert remove_html_markup("'<b>foo</b>'")
    assert remove_html_markup("<'b'>foo</'b'>")
