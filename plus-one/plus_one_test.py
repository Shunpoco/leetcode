import unittest

from plus_one import Solution

class TestPlusOne(unittest.TestCase):
    def setUp(self):
        self.testCases = [
            {
                'digits': [1, 2, 3],
                'expected': [1, 2, 4],
            },
            {
                'digits': [4, 3, 2, 1],
                'expected': [4, 3, 2, 2],
            },
            {
                'digits': [1, 2, 3, 9],
                'expected': [1, 2, 4, 0],
            },
            {
                'digits': [9, 9, 9, 9],
                'expected': [1, 0, 0, 0, 0],
            },
            {
                'digits': [0, 0, 0, 0],
                'expected': [0, 0, 0, 1],
            },
        ]


    def test(self):
        s = Solution()

        for testCase in self.testCases:
            with self.subTest(testCase=testCase):
                self.assertEqual(
                    s.plusOne(testCase['digits']),
                    testCase['expected'],
                )

    def tearDown(self):
        print('Happy holiday!')

if __name__ == '__main__':
    unittest.main()
