import unittest

from check import Solution

class TestCheckIfExist(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
        self.testCases = [
            {
                'arr': [10, 2, 5, 3],
                'want': True,
            },
            {
                'arr': [7,1,14,11],
                'want': True,
            },
            {
                'arr': [3,1,7,11],
                'want': False,
            },
            {
                'arr': [0, 0],
                'want': True,
            },
            {
                'arr': [4,-7,11,4,18],
                'want': False,
            },
        ]

    def test(self):
        for tc in self.testCases:
            with self.subTest(tc=tc):
                self.assertEqual(
                    self.solution.checkIfExist(tc['arr']),
                    tc['want'],
                )

if __name__ == '__main__':
    unittest.main()
