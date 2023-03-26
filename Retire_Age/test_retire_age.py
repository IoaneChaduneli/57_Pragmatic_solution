from retire_age import calculate_retire_year

def test_calculate_retire_year():
    assert calculate_retire_year('20', '65') == f"You will retire after {45} years later\n You will retire in {2068}"


def test_already_retire():
    assert calculate_retire_year('70', '65') == f"You retired {abs(5)} years ago\nYou retired in {2018}"


def test_retire_year_invalid():
    assert calculate_retire_year('hy3', 65) == f"Please write numeric value"