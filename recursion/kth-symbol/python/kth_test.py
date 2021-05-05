import unittest

from kth import Solution

class TestKth(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

        self.testCases = [
            {
                'N': 1,
                'K': 1,
                'want': 0,
            },
            {
                'N': 2,
                'K': 1,
                'want': 0,
            },
            {
                'N': 2,
                'K': 2,
                'want': 1,
            },
            {
                'N': 4,
                'K': 5,
                'want': 1,
            },
        ]

    def test(self):
        for tc in self.testCases:
            with self.subTest(tc=tc):
                self.assertEqual(
                    self.s.kthGrammar(tc['N'], tc['K']),
                    tc['want'],
                )

if __name__ == '__main__':
    unittest.main()
