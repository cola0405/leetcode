# lower bound 最小是len(lst) -- 比列表里面的元素都大
# upper bound 最大是len(lst)
# 只是用于区分当有相等元素时，把元素插入到哪里！！！

from typing import List

class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        def check(radius):
            i = 0
            j = 0
            # 双指针检测当前radius是否可行
            while i<len(houses):
                left = heaters[j]-radius
                right = heaters[j]+radius
                if houses[i]<left or (j==len(heaters)-1 and houses[i]>right):
                    return False
                while i<len(houses) and left<=houses[i]<=right:
                    i += 1
                if i == len(houses):
                    return True
                if j<len(heaters)-1:
                    j += 1
            return True

        houses.sort()
        heaters.sort()

        low = 0
        high = max(max(houses), max(heaters))
        while low<high:
            mid = (low+high)//2
            if check(mid):
                high = mid
            else:
                low = mid+1

        return low

print(Solution().findRadius(houses = [1,5], heaters = [10]))

