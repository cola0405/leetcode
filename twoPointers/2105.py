from typing import List
class Solution:
    def minimumRefill(self, plants: List[int], capacityA: int, capacityB: int) -> int:
        i = 0
        j = len(plants)-1
        a = capacityA
        b = capacityB

        ans = 0
        while i <= j:
            if i == j:
                if max(a,b) < plants[i]:
                    ans += 1
                break

            if a < plants[i]:
                a = capacityA
                ans += 1

            if b < plants[j]:
                b = capacityB
                ans += 1

            a -= plants[i]
            b -= plants[j]
            i += 1
            j -= 1
        return ans

print(Solution().minimumRefill([1,2,4,4,5], 6, 5))