import unittest

from fibonacci import Solution

class TestFibonacci(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

        self.testCases = [
            {
                'n': 2,
                'want': 1,
            },
            {
                'n': 3,
                'want': 2,
            },
            {
                'n': 4,
                'want': 3,
            },
            {
                'n': 30,
                'want': 832040,
            },
        ]

    def test(self):
        for tc in self.testCases:
            with self.subTest(tc=tc):
                self.assertEqual(
                    self.s.fib(tc['n']),
                    tc['want'],
                )

if __name__ == '__main__':
    unittest.main()

