# data restructuring
from typing import List
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)
        cars = sorted([(position[i], speed[i]) for i in range(n)])
        t = [(target-pos) / sp for pos, sp in cars]     # arrive time
        for i in range(n-1)[::-1]:
            if t[i] < t[i+1]:   # when needed time is less than [i+1], which means you can merge them
                t[i] = t[i+1]
        return len(set(t))
print(Solution().carFleet(target = 17, position =[8,12,16,11,7], speed = [6,9,10,9,7]))
