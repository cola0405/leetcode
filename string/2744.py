from typing import List
class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        n = len(words)
        already = set()
        ans = 0
        for i in range(n):
            if i in already:
                continue
            for j in range(i+1, n):
                if j in already:
                    continue
                if words[i] == words[j][::-1]:
                    ans += 1
                    already.add(i)
                    already.add(j)
        return ans