from typing import List
class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        n = len(arr)
        right = [-1]*n
        for i in range(n):
            for j in range(i+1, n)[::-1]:
                if arr[j] < arr[i]:
                    right[i] = j
                    break
        ans = 0
        cur = 0
        while cur < n:
            if right[cur] == -1:
                cur += 1
            else:
                # check interval
                end = right[cur]+1
                k = cur
                while k < end:
                    end = max(end, right[k]+1)
                    k += 1
                cur = end
            ans += 1
        return ans

print(Solution().maxChunksToSorted([1,4,0,2,3,5]))