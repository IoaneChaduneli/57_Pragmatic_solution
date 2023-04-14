from rectangular import calculate_sqf, sqf_to_sqm

def test_calculate_sqf():
    assert calculate_sqf('5', '10') == 50.0

def test_sqf_to_sqm():
    assert sqf_to_sqm(5, 10) == 4.65

