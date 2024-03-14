# c[i] = a[i] + b[i] to make problem easier
# c[i] can be considered that "I Got You Lose"
# we need to get the maximum c[i] every time to make the optimal operation
from typing import List
class Solution:
    def stoneGameVI(self, aliceValues: List[int], bobValues: List[int]) -> int:
        n = len(aliceValues)
        arr = [(aliceValues[i]+bobValues[i], i) for i in range(n)]
        arr.sort(reverse=True)
        alice = 0
        bob = 0
        for i in range(n):
            if i%2 == 0:
                alice += aliceValues[arr[i][1]]
            else:
                bob += bobValues[arr[i][1]]
        if alice > bob:
            return 1
        elif alice < bob:
            return -1
        else:
            return 0

print(Solution().stoneGameVI([1,2],[3,1]))
