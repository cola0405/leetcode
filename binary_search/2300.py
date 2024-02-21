from typing import List
class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        ans = []
        for s in spells:
            low = 0
            high = len(potions)-1
            while low < high:
                mid = (low+high)//2
                if s * potions[mid] >= success:
                    high = mid
                else:
                    low = mid+1
            if s*potions[low] >= success:
                ans.append(len(potions) - low)
            else:
                ans.append(0)
        return ans