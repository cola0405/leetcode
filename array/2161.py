from typing import List
class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        p1 = []
        p2 = []
        p3 = []
        for num in nums:
            if num < pivot:
                p1.append(num)
            elif num == pivot:
                p2.append(num)
            else:
                p3.append(num)
        return p1+p2+p3