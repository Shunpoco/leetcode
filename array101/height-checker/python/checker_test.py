import unittest

from checker import Solution

class TestHeightChecker(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

        self.testCases = [
            {
                'heights': [1,1,4,2,1,3],
                'want': 3,
            },
            {
                'heights': [5,1,2,3,4],
                'want': 5,
            },
            {
                'heights': [1,2,3,4,5],
                'want': 0,
            },
        ]

    def test(self):
        for tc in self.testCases:
            with self.subTest(tc=tc):
                self.assertEqual(
                    self.s.heightChecker(tc['heights']),
                    tc['want'],
                )

if __name__ == '__main__':
    unittest.main()
