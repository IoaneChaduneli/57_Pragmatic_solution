from counter_string import calculate_string_length

def test_calculate_string_length():
    assert calculate_string_length("Please enter the text: ") == 11

def test_calculate_letters_and_numbers_length():
    assert calculate_string_length("Please enter the text: ") == ''

def test_calculate_numbers_string_length():
    assert calculate_string_length("Please enter the text: ") == ''