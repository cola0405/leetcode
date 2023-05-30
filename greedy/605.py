from typing import List
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0:
            return True
        i = 0
        while i<len(flowerbed):
            if flowerbed[i] == 1:
                pass
            # 能到elif 已经说明了flowerbed[i] = 0
            elif i == len(flowerbed)-1 or flowerbed[i+1] == 0:
                n -= 1
                if n <= 0:
                    return True
            else:
                i += 1
            i += 2
        return False

print(Solution().canPlaceFlowers(flowerbed = [1,0,0,0,1,0,0], n = 2))