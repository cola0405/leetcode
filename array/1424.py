# diagonal hash
# index i+j of elements in the same diagonal will be the same
# we can use hash map to store the elements in the same diagonal
from typing import List
class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        from collections import defaultdict
        d = defaultdict(list)
        n = len(nums)
        max_size = 0
        for i in range(n)[::-1]:
            max_size = max(max_size, len(nums[i]))
            for j in range(len(nums[i])):
                d[i+j].append(nums[i][j])       # store the elements in the diagonal

        ans = []
        for i in range(n-1+max_size):
            for num in d[i]:
                ans.append(num)
        return ans


print(Solution().findDiagonalOrder([[1,2,3],[4,5,6],[7,8,9]]))