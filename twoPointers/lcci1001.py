from typing import List
class Solution:
    def merge(self, A: List[int], m: int, B: List[int], n: int) -> None:
        """
        Do not return anything, modify A in-place instead.
        """
        for i in range(m):
            A[-i-1] = A[m-i-1]
        i = n
        j = 0
        cur = 0
        for cur in range(m+n):
            if i == m+n or j == n:
                break
            if A[i] < B[j]:
                A[cur] = A[i]
                i += 1
            else:
                A[cur] = B[j]
                j += 1
        while j < n:
            A[cur] = B[j]
            cur += 1
            j += 1

print(Solution().merge(A = [1,2,3,0,0,0], m = 3,
B = [2,5,6],       n = 3))