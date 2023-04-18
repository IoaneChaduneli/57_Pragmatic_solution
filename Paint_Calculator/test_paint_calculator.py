import unittest
from paint_calculator import sqf_to_sqm, room_sqm, ballon_neccassity

# sqf_to_sqm
class TestSqfSqm(unittest.TestCase):
    def test_valid(self):
        result = sqf_to_sqm(10)
        self.assertEqual(result, 0.9290304)

#room_sqm
class TestRoomSqm(unittest.TestCase):
    def test_valid(self):
        result = room_sqm(10,5)
        self.assertEqual(result, 0.43154874206208005)

#ballon_neccassity
class BallonNeccasity(unittest.TestCase):
    def vald_argument(self):
        result = ballon_neccassity(10,5)
        self.assertEqual(result, 'You will need to purchase 1 gallons of paint to cover 4 sqare meter')

    def test_invalid_argument(self):
        with self.assertRaises(ValueError):
            ballon_neccassity('frt', 'ght')


if __name__ == '__main__':
    unittest.main()