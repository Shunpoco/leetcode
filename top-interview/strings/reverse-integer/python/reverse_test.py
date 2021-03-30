import unittest

from reverse import Solution

class TestReverseInteger(unittest.TestCase):
    def setUp(self):
        self.testCases = [
            {
                'x': 123,
                'want': 321,
            },
            {
                'x': -123,
                'want': -321,
            },
            {
                'x': 0,
                'want': 0,
            },
            {
                'x': 120,
                'want': 21,
            },
            {
                'x': 1563847412,
                'want': 0,   
            },
            {
                'x': -1563847412,
                'want': 0,
            },
            {
                'x': -1563840,
                'want': -483651,
            },
            {
                'x': 14500000,
                'want': 541,
            },
        ]

    def test(self):
        s = Solution()
        for tc in self.testCases:
            with self.subTest(testCase=tc):
                self.assertEqual(
                    s.reverse(tc['x']),
                    tc['want'],
                )

if __name__ == '__main__':
    unittest.main()
