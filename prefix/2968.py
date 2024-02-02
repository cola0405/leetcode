# mid-greedy -- 1/2 index
# sliding window

# the most frequent element must be in the interval -- window
# under the cost<=k, all the numbers in window can turn into the target
# then we need to find out the longest window with the cost <= k
# the target should be the mid(1/2 index) -- closest to all numbers in window
# the cost can be divided into two parts -- left and right
from typing import List
class Solution:
    def maxFrequencyScore(self, nums: List[int], k: int) -> int:
        nums.sort()
        i,j = 0,1
        left, right = 0,0
        left_cnt, right_cnt = 0,0
        mid = 0
        ans = 1
        while i < len(nums):    # two pointers for sliding window
            while j < len(nums):
                cost = (left_cnt*nums[mid] - left) + (right - right_cnt*nums[mid])
                if cost > k:
                    break

                score = j-i
                ans = max(ans, score)

                right += nums[j]
                right_cnt += 1
                if (j-i)%2 == 0:
                    left += nums[mid]
                    left_cnt += 1

                    mid += 1  # mid move to right by 1
                    right -= nums[mid]
                    right_cnt -= 1
                j += 1

            # we do need it for the situation -- window shrink in the end
            cost = (left_cnt*nums[mid] - left) + (right - right_cnt*nums[mid])
            if cost <= k:
                ans = max(ans, j-i)

            # here cost > k, we need to pop the left
            if (j-i) % 2 == 0:  # when the window size is even, the mid should be updated
                left += nums[mid]   # when the mid is updated, the left also need to be updated
                left_cnt += 1
                mid += 1
                right -= nums[mid]
                right_cnt -= 1

            left -= nums[i]
            left_cnt -= 1
            i += 1

        return ans

print(Solution().maxFrequencyScore(nums = [10,26,21,18,30,25,1], k = 8))




