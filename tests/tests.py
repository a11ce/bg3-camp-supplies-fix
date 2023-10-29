# test_my_code.py

import unittest
import runner

class TestInventories(unittest.TestCase):
    def test_not_enough_items(self):
        result = runner.process_inv_file('../inventories/not_enough.txt')
        self.assertEqual(sum_value(result), 14)


def sum_value(inv: list):
    sum = 0
    for item in inv:
        sum += runner.supplies[item]
    return sum

if __name__ == '__main__':
    unittest.main()