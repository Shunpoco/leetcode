import unittest

from add_binary import Solution

class TestAddBinary(unittest.TestCase):
    def setUp(self):
        self.testCases = [
            {
                'a': '11',
                'b': '1',
                'expected': '100',
            },
            {
                'a': '1010',
                'b': '1011',
                'expected': '10101',
            },
            {
                'a': '1111',
                'b': '000',
                'expected': '1111',
            },
            {
                'a': '1010',
                'b': '000000',
                'expected': '1010',
            },
            {
                'a': '0',
                'b': '0',
                'expected': '0',
            },
        ]

    def test(self):
        s = Solution()
        for testCase in self.testCases:
            with self.subTest(testCase=testCase):
                self.assertEqual(
                    s.addBinary(testCase['a'], testCase['b']),
                    testCase['expected'],
                )

if __name__ == '__main__':
    unittest.main()
