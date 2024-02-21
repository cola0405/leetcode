from typing import List
class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()

        j = 0
        ans = 0
        for i in range(len(trainers)):
            if players[j] <= trainers[i]:
                ans += 1
                j += 1
            if j == len(players):
                return j
        return j

print(Solution().matchPlayersAndTrainers(players = [4,7,9], trainers = [8,2,5,8]))