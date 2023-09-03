from typing import List
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        import random
        def quick_sort(start, end):
            if start >= end:
                return
            mid = nums[random.randint(start,end)]
            i = start
            j = end
            while i<j:
                while i<j and nums[j] >= mid:
                    j -= 1
                nums[i] = nums[j]
                while i<j and nums[i] < mid:
                    i += 1
                nums[j] = nums[i]
            nums[i] = mid

            quick_sort(start, i-1)
            quick_sort(i+1, end)

        quick_sort(0,len(nums)-1)
        return nums[-k]

print(Solution().findKthLargest([3,2,1,5,6,4],2))






