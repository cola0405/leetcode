from typing import List
class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        count = {}
        for num in deck:
            count[num] = count.get(num,0)+1
        for x in range(2, min(count.values())+1):
            for val in count.values():
                if val%x != 0:
                    break
            else:
                return True
        return False

print(Solution().hasGroupsSizeX(deck = [1,1,1,2,2,2,3,3]))
