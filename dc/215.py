# 每次用快排的分割方法
# 如果当前分割情况不符合k，则进行类二分调整

from typing import List
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        n = len(nums)
        def partition():
            pivot = nums[mid]
            i,j = low, high
            while i<j:
                # 分割应该采取待定-推进模式
                while j-1 >= 0 and nums[j] > pivot:
                    j -= 1
                while i+1 < n and nums[i] < pivot:
                    i += 1
                if nums[i] > pivot:
                    nums[i], nums[j] = nums[j], nums[i]
                    j -= 1
                elif nums[j] < pivot:
                    nums[i],nums[j] = nums[j], nums[i]
                    i += 1
                else:
                    j -= 1  # 处理[2,2,2,2]这种油盐不进的
            return i


        low = 0
        high = n-1
        while low<high:
            mid = (low+high+1)//2
            idx = partition()
            if idx == len(nums)-k:
                return nums[idx]
            elif idx > n-k:
                high = idx-1  # !!不是mid哈，是分割、调整好后的idx
            else:
                low = idx+1
        return nums[low]

print(Solution().findKthLargest([-1,2,0],
2))

"""
[3,2,1,5,6,4],
2

5


[-1,2,0],
2

0
"""
