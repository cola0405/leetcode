# 每次让n-1个元素加1，相当于让某一个元素减1
# 则问题转化为操作多少次，可以让所有数都减到min
from typing import List
class Solution:
    def minMoves(self, nums: List[int]) -> int:
        min_value = min(nums)
        ans = 0
        for num in nums:
            ans += num - min_value
        return ans
