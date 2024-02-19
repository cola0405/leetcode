from typing import List
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        def fit(length):
            i = 0
            cnt = 0
            for inx in range(length):
                if nums[inx] == 1:
                    cnt += 1
            if cnt + k >= length:
                return True

            for j in range(length, n):
                if nums[i] == 1:
                    cnt -= 1
                if nums[j] == 1:
                    cnt += 1
                if cnt + k >= length:
                    return True
                i += 1
            return False

        n = len(nums)
        low = 0
        high = n
        while low < high:
            mid = (low+high+1)//2
            if fit(mid):
                low = mid
            else:
                high = mid-1
        return low

print(Solution().longestOnes([0,0,1,1,1,0,0], 0))