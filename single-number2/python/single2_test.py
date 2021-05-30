import unittest
from single2 import Solution


class TestSingleNumber(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

        self.testCases = [
            {
                'nums': [2,2,3,2],
                'want': 3,
            },
            {
                'nums': [0,1,0,1,0,1,99],
                'want': 99,
            },
        ]


    def test(self):
        for tc in self.testCases:
            with self.subTest(tc=tc):
                self.assertEqual(
                    self.s.singleNumber(tc['nums']),
                    tc['want'],
                )


if __name__ == '__main__':
    unittest.main()
