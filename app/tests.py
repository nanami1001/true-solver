# tests.py
# 測試核心邏輯

import unittest
from solver import find_expression

class SolverTestCase(unittest.TestCase):
    def test_known_values(self):
        self.assertEqual(eval(find_expression(24)), 24)
        self.assertEqual(eval(find_expression(0)), 0)

    def test_invalid(self):
        self.assertIsNone(find_expression(99999))

if __name__ == '__main__':
    unittest.main()