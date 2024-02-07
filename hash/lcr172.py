from typing import List
class Solution:
    def countTarget(self, scores: List[int], target: int) -> int:
        from collections import Counter
        return Counter(scores)[target]