from typing import List
class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        import heapq

        min_idx = 0
        max_idx = 0
        n = len(nums)

        # 单调栈
        for_min = []
        for_max = []
        for i in range(1,n):
            if i-min_idx>indexDiff:
                min_idx = heapq.heappop(for_min)[1]
            if i-max_idx>indexDiff:
                max_idx = heapq.heappop(for_max)[1]

            if i-min_idx <= indexDiff and abs(nums[i] - nums[min_idx]) <= valueDiff:
                return True
            if i-max_idx <= indexDiff and abs(nums[i] - nums[max_idx]) <= valueDiff:
                return True

            heapq.heappush(for_min, (nums[i], i))
            heapq.heappush(for_max, (-nums[i], i))

            if nums[i] < nums[min_idx]:
                min_idx = i
                for_min = []
            if nums[i] > nums[max_idx]:
                max_idx = i
                for_max = []
        return False

print(Solution().containsNearbyAlmostDuplicate(nums = [4,1,6,3], indexDiff = 4, valueDiff = 1))