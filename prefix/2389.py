from typing import List
class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()  # 没要求递增，就无所谓
        ans = []
        for target in queries:
            s = 0
            for i in range(len(nums)):
                s += nums[i]
                if s >= target:
                    break
            if s > target:
                ans.append(i)
            else:
                ans.append(i+1)
        return ans

print(Solution().answerQueries(nums = [4,5,2,1], queries = [3,10,21]))

