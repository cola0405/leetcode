from typing import List
class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        n = len(arr)
        arr.sort()
        min_diff = float('inf')
        for i in range(n-1):
            min_diff = min(min_diff, arr[i+1]-arr[i])
        ans = []
        for i in range(n-1):
            if arr[i+1]-arr[i] == min_diff:
                ans.append([arr[i],arr[i+1]])
        return ans

print(Solution().minimumAbsDifference([4,2,1,3]))