from simple_math import math_operation

def test_math_operation():
    assert math_operation('10', '5') == f"{10} + {5} = {15}\n{10} - {5} = {5}\n{10} * {5} = {50}\n{10} / {5} = {2.0}"


def test_negative_math_operation():
    assert math_operation('10','-5') == f'It is not possible prompt to be negative or non-numeric value'


def test_non_numeric_math_operation():
    assert math_operation('iy4', 5) == f'It is not possible prompt to be negative or non-numeric value'