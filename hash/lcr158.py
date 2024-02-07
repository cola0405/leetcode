from typing import List
class Solution:
    def inventoryManagement(self, stock: List[int]) -> int:
        from collections import Counter
        cnt = Counter(stock)
        for i in cnt:
            if cnt[i] > len(stock)/2:
                return i