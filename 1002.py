from typing import List


class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        count = {chr(i): float('inf') for i in range(97,123)}
        for ch in count:
            for word in words:
                count[ch] = min(word.count(ch), count[ch])
        res = []
        for ch in count:
            if count[ch] != float('inf'):
                res += [ch]*count[ch]
        return res



print(Solution().commonChars(words = ["bella","label","roller"]))