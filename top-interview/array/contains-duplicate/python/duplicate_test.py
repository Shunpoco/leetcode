import unittest

from duplicate import Solution

class TestDuplicate(unittest.TestCase):
    def setUp(self):
        self.testCases = [
            {
                'nums': [1,2,3,1],
                'want': True,
            },
            {
                'nums': [1,2,3,4],
                'want': False,
            },
            {
                'nums': [1,1,1,3,3,4,3,2,4,2],
                'want': True,
            },
        ]

    def test(self):
        s = Solution()
        for tc in self.testCases:
            with self.subTest(testCase=tc):
                self.assertEqual(
                    s.containsDuplicate(tc['nums']),
                    tc['want'],
                )

if __name__ == '__main__':
    unittest.main()