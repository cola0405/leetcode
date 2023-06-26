from typing import List
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        flowerbed.append(0)
        i = 0
        while i+1<len(flowerbed):
            if flowerbed[i] == 0:
                if i+1<len(flowerbed) and flowerbed[i+1]==0:
                    n -= 1
                    i += 1
            else:
                i += 1
            i += 1
        return n <= 0

print(Solution().canPlaceFlowers([1,0,0,0,0,1],
2))

