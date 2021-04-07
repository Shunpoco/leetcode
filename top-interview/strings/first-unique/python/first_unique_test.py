import unittest

from first_unique import Solution

class TestFirstUniqueChar(unittest.TestCase):
    def setUp(self):
        self.testCases = [
            {
                's': 'leetcode',
                'want': 0,
            },
            {
                's': 'loveleetcode',
                'want': 2,
            },
            {
                's': 'aabb',
                'want': -1
            },
        ]

        self.s = Solution()

    def test(self):
        for tc in self.testCases:
            with self.subTest(tc=tc):
                self.assertEqual(
                    self.s.firstUniqChar(tc['s']),
                    tc['want'],
                )

if __name__ == '__main__':
    unittest.main()
