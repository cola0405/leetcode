from typing import List
class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        from collections import Counter
        nums = []
        n = len(grid)
        for i in range(n):
            for j in range(n):
                nums.append(grid[i][j])

        ans = [0,0]
        cnt = Counter(nums)
        for num in range(1,n**2+1):
            if cnt[num] == 2:
                ans[0] = num
            elif cnt[num] == 0:
                ans[1] = num
        return ans