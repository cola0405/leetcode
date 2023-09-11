# 困难是因为题目要求用常量级别的空间
# 一般是要swap操作了
from typing import List
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        already = set()
        ans = 1
        for num in nums:
            if num == ans:
                ans += 1
                while ans in already:
                    ans += 1    # 如果ans+1之前已经出现过了呢
            already.add(num)
        return ans

print(Solution().firstMissingPositive())
