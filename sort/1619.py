from typing import List
class Solution:
    def trimMean(self, arr: List[int]) -> float:
        n = len(arr)
        arr.sort()
        x = int(n*0.05)
        return sum(arr[x:n-x]) / (n-2*x)
