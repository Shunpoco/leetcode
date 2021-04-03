import unittest

from plus_one import Solution


class TestPlusOne(unittest.TestCase):
    def setUp(self):
        self.s = Solution()
        self.testCases = [
            {
                'digits': [1,2,3],
                'want': [1,2,4],
            },
            {
                'digits': [4,3,2,1],
                'want': [4,3,2,2],
            },
            {
                'digits': [0],
                'want': [1],
            },
            {
                'digits': [1,2,3,9],
                'want': [1,2,4,0],
            },
            {
                'digits': [9,9,9],
                'want': [1,0,0,0],
            },
        ]

    def test(self):
        for tc in self.testCases:
            with self.subTest(tc=tc):
                self.assertEqual(
                    self.s.plusOne(tc['digits']),
                    tc['want'],
                )

if __name__ == '__main__':
    unittest.main()
