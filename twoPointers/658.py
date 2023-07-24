from typing import List
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        from collections import deque
        ans = deque([])
        n = len(arr)
        for i in range(n):
            if arr[i]>x:
                break
        j = i
        i = j-1
        while 0<=i<n and 0<=j<n and len(ans)<k:
            if j > len(arr) or x-arr[i] <= arr[j]-x:
                ans.appendleft(arr[i])
                i -= 1
            else:
                ans.append(arr[j])
                j += 1
        # 放心后置处理
        while 0<=i<n and len(ans)<k:
            ans.appendleft(arr[i])
            i -= 1
        while 0<=j<n and len(ans)<k:
            ans.append(arr[j])
            j += 1
        return list(ans)

print(Solution().findClosestElements([-2,-1,1,2,3,4,5],
7,
3))

