
from tip_calculator import tip_calculator, check_calculator

def test_tip_calculator():
    assert tip_calculator(11.25,15) == 1.69

def test_check_calculator():
    assert check_calculator('8') == 8.64