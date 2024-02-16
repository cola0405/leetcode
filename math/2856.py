# math

# we need to find out that the nums[i] can be used for the previous and after numbers

# max_cnt is the keypoint
# if max_cnt*2 > n, which means max_cnt is already more than all other numbers -- they can be paired
# in this situation, the remaining numbers must falls in max_cnt and equal to (max_cnt*2 - n)
# hint: actually it comes from n - 2*(n-max_cnt) = max_cnt*2 - n

# if max_cnt*2 < n, which means all the numbers could be paired and without remain numbers
# but when n is odd, which means there do have 1 number could not be paired


from typing import List
class Solution:
    def minLengthAfterRemovals(self, nums: List[int]) -> int:
        from collections import Counter
        cnt = Counter(nums)
        max_cnt = max(cnt.values())
        if max_cnt*2 > len(nums):
            return max_cnt*2 - len(nums)
        else:
            return len(nums)%2


print(Solution().minLengthAfterRemovals([1,1,2]))