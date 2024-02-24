from typing import List
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        from collections import defaultdict
        s = set(arr2)
        cnt = defaultdict(int)
        arr3 = []

        for num in arr1:
            if num in s:
                cnt[num] += 1
            else:
                arr3.append(num)

        ans = []
        for num in arr2:
            ans += [num]*cnt[num]
        return ans + sorted(arr3)