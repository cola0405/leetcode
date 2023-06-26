from typing import List
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if flowerbed == [0]:
            return True
        i = 0
        while i<len(flowerbed):
            if flowerbed[i] == 0 \
                and (((i+1<len(flowerbed) and flowerbed[i+1]==0) and (i>0 and flowerbed[i-1]==0))
                or (i==0 and i+1<len(flowerbed) and flowerbed[i+1]==0)
                or (i==len(flowerbed)-1 and i-1>=0 and flowerbed[i-1]==0)):
                n -= 1
                flowerbed[i] = 1
                i += 1
            i += 1
        return n <= 0