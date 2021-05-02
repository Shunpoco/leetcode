import unittest

from pascal import Solution

class TestPascal(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

        self.testCases = [
            {
                'rowIndex': 3,
                'want': [1,3,3,1],
            },
            {
                'rowIndex': 0,
                'want': [1],
            },
            {
                'rowIndex': 1,
                'want': [1, 1],
            },
        ]

    def test(self):
        for tc in self.testCases:
            with self.subTest(tc=tc):
                self.assertEqual(
                    self.s.getRow(tc['rowIndex']),
                    tc['want'],
                )

if __name__ == '__main__':
    unittest.main()
