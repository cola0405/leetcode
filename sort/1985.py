from typing import List
class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        arr = sorted(map(int, nums), reverse=True)
        return str(arr[k-1])

print(Solution().kthLargestNumber(["3","6","7","10"], k = 4))