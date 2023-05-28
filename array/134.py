from typing import List
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        low_gas = 0
        pos = -1
        available = 0
        for i in range(len(gas)):
            available += gas[i] - cost[i]
            if available<low_gas:
                low_gas = available
                pos = i
        if sum(gas) >= sum(cost):
            return pos+1
        return -1

print(Solution().canCompleteCircuit(gas = [1,2,3,4,5], cost = [3,4,5,1,2]))