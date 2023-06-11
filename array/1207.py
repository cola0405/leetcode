from typing import List
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        from collections import defaultdict
        count = defaultdict(int)
        for num in arr:
            count[num] += 1
        if len(count) == len(set(count.values())):
            return True
        return False

print(Solution().uniqueOccurrences(arr = [1,2,2,1,1,3]))
