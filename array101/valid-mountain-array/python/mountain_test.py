import unittest

from mountain import Solution

class TestValidMountain(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

        self.testCases = [
            {
                'arr': [2,1],
                'want': False,
            },
            {
                'arr': [3,5,5],
                'want': False,
            },
            {
                'arr': [0,3,2,1],
                'want': True,
            },
            {
                'arr': [0,2,3,3,5,2,1,0],
                'want': False
            },
            {
                'arr': [0,2,3,4,5,2,1,0],
                'want': True,
            },
            {
                'arr': [0,1,2,3,4,5,6,7],
                'want': False,
            },
            {
                'arr': [9,8,7,6,5,4,3,2],
                'want': False,
            },
        ]

    def test(self):
        for tc in self.testCases:
            with self.subTest(tc=tc):
                self.assertEqual(
                    self.solution.validMountainArray(tc['arr']),
                    tc['want'],
                )

if __name__ == '__main__':
    unittest.main()
