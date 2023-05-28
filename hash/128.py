from typing import List
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        ans = 0
        for num in s:
            if num-1 not in s:  # 剪枝操作（这个连续序列没有比它更小的，那么延展出去，得到的就是极限值）
                count = 1
                while num+1 in s:
                    num += 1
                    count += 1
                ans = max(count, ans)
        return ans

print(Solution().longestConsecutive(nums = [9,1,4,7,3,-1,0,5,8,-1,6]))