import unittest

from find import Solution

class TestFindDisappearedNumbers(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

        self.testCases = [
            {
                'nums': [4,3,2,7,8,2,3,1],
                'want': [5,6],
            },
            {
                'nums': [1,1],
                'want': [2],
            },
        ]

    def test(self):
        for tc in self.testCases:
            with self.subTest(tc=tc):
                self.assertEqual(
                    self.s.findDisappearedNumbers(tc['nums']),
                    tc['want'],
                )

if __name__ == '__main__':
    unittest.main()
