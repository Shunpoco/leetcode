import unittest

from mypow import Solution

class TestPow(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

        self.testCases = [
            {
                'x': 2.0,
                'n': 10,
                'want': 1024.00000,
            },
            {
                'x': 2.1,
                'n': 3,
                'want': 9.26100,
            },
            {
                'x': 2.0,
                'n': -2,
                'want': 0.25000,
            },
        ]

    def test(self):
        for tc in self.testCases:
            with self.subTest(tc=tc):
                self.assertAlmostEqual(
                    self.s.myPow(tc['x'], tc['n']),
                    tc['want'],
                    places=5,
                )

if __name__ == '__main__':
    unittest.main()
