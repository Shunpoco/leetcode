class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort(reverse=True)
        trainers.sort(reverse=True)

        result = 0

        it = 0
        for p in players:
            if it >= len(trainers):
                break
            if p <= trainers[it]:
                result += 1
                it += 1
            
        return result

