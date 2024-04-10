class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        n = len(deck)
        deck.sort()

        queue = deque()
        queue.append(deck[n-1])

        for i in range(n-2, -1, -1):
            queue.appendleft(queue.pop())
            queue.appendleft(deck[i])

        result = []
        while queue:
            result.append(queue.popleft())

        return result

