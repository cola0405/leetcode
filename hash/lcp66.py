from typing import List
class Solution:
    def minNumBooths(self, demand: List[str]) -> int:
        from collections import defaultdict, Counter
        min_demand = defaultdict(int)
        for stages in demand:
            count = Counter(stages)
            for booth in count:
                min_demand[booth] = max(min_demand[booth], count[booth])
        return sum(min_demand.values())