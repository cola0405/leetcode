from typing import List
class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        n = len(arr)
        i = n-1
        for j in range(n)[::-1]:
            if arr[j] != 0:
                arr[i] = arr[j]
                i -= 1

        for j in range(i):
            arr[j] = 0
