from stack_queue_brackets import validate_brackets

def test_example_1():
    assert validate_brackets("{}") == True

def test_example_2():
    assert validate_brackets("{}(){}") == True

def test_example_3():
    assert validate_brackets("()[[Extra Characters]]") == True

def test_example_4():
    assert validate_brackets("(){}[[]]") == True

def test_example_5():
    assert validate_brackets("(](") == False

def test_example_6():
    assert validate_brackets("{(})") == False
