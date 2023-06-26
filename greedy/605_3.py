from typing import List
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        flowerbed.append(0)
        flowerbed.insert(0,0)
        i = 0
        while i<=len(flowerbed)-3:
            if flowerbed[i]==0 and flowerbed[i+1]==0 and flowerbed[i+2]==0:
                n -= 1
                flowerbed[i+1] = 1
            i += 1
        return n <= 0

print(Solution().canPlaceFlowers([1,0,0,0,0,1],
2))

