import unittest

from replace_elements import Solution

class TestReplaceElements(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

        self.testCases = [
            {
                'arr': [17, 18, 5, 4, 6, 1],
                'want': [18, 6, 6, 6, 1, -1],
            },
        ]

    def test(self):
        for tc in self.testCases:
            with self.subTest(tc=tc):
                self.assertEqual(
                    self.s.replaceElements(tc['arr']),
                    tc['want'],
                )

if __name__ == '__main__':
    unittest.main()
