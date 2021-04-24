import unittest

from parity import Solution

class TestSortArray(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

        self.testCases = [
            {
                'A': [3,1,2,4],
                'want': [2,4,3,1],
            },
            {
                'A': [1],
                'want': [1],
            },
            {
                'A': [0,1],
                'want': [0,1],
            },
            {
                'A': [2,4,3,1],
                'want': [2,4,3,1],
            },
        ]

    def test(self):
        for tc in self.testCases:
            with self.subTest(tc=tc):
                self.assertEqual(
                    self.s.sortArrayByParity(tc['A']),
                    tc['want'],
                )

if __name__ == '__main__':
    unittest.main()
