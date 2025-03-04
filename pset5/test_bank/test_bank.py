from bank import value

def test_bank():
	assert value("hello") == 0
	assert value("HELLO") == 0

def test_valid():
	assert value("how are you?") == 20
	assert value("what is this?") == 100
