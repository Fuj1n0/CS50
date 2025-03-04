from twttr import shorten

def test_shorten():
    assert shorten("AEIOU") == ""
    assert shorten("aeiou") == ""
    assert shorten("CS50") == "CS50"
    assert shorten("Python") == "Pythn"
    assert shorten("What's your name?") == "Wht's yr nm?"

