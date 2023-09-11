from typing import List
class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        import heapq
        window = []

        n = len(nums)
        for i in range(n):
            heapq.heappush(window, n)
            heapq.