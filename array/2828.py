from typing import List
class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        head = ''
        for word in words:
            head += word[0]
        return head == s