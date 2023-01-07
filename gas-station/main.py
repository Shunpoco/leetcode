from typing import List

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        start = -1
        diffs = [0] * len(gas)
        m_diff = 0

        for i, (g, c) in enumerate(zip(gas, cost)):
            diffs[i] = g - c
            if m_diff == 0 and diffs[i] >= 0:
                m_diff = diffs[i]
                start = i
            else:
                m_diff +=  diffs[i]
                if m_diff < 0:
                    m_diff = 0
                    start = -1

        if start == -1:
            return start

        s = 0
        for i in range(len(gas)):
            s += diffs[(start+i)%len(gas)]
            if s < 0:
                return -1

        return start
