from typing import List
class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        from collections import Counter
        frequency = Counter(arr).most_common()
        amount = 0
        for i in range(len(frequency)):
            num, count = frequency[i]
            amount += count
            if amount >= len(arr)//2:
                return i+1

print(Solution().minSetSize(arr = [9,77,63,22,92,9,14,54,8,38,18,19,38,68,58,19]))
