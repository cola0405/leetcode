from typing import List
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        citations.sort()
        for i in range(len(citations)):
            if citations[i] >= n-i:
                return n-i
        return 0