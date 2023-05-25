from typing import List
class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        res = []
        for ch in set(words[0]):
            count = float('inf')
            for word in words:
                count = min(word.count(ch), count)
            res += [ch]*count
        return res

print(Solution().commonChars(words = ["bella","label","roller"]))