class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        n = len(hand)
        if n % groupSize != 0:
            return False

        hand.sort()
        for i in range(n):
            if hand[i] >= 0:
                if not self.grouping(hand, i, n, groupSize):
                    return False

        return True

    def grouping(self, hand, i, n, groupSize):
        nv = hand[i] + 1
        hand[i] = -1
        c = 1
        i += 1
        while i < n and c < groupSize:
            if hand[i] == nv:
                nv += 1
                c += 1
                hand[i] = -1

            i += 1

        return c == groupSize


