from quotes import discover_phrase

def test_discover_phrase():
    base = [
        {
            'author': 'Ioane the Great',
            'phrase': 'Keep push yourself, untill you see the certenity of work',
        }
    ]
    assert discover_phrase(base) == 'Ioane the Great says, "Keep push yourself, untill you see the certenity of work"'


def invalid_test_discover_phrase():
    base_1 = [
        {
            'author': '',
            'phrase': ''
        }
    ]
    assert discover_phrase(base_1) == f'False Value'