from typing import List
class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        w = [word.count(min(word)) for word in words]
        w.sort(reverse=True)
        ans = []
        for q in queries:
            f = q.count(min(q))
            count = 0
            for amount in w:
                if f >= amount:
                    break
                count += 1
            ans.append(count)
        return ans

print(Solution().numSmallerByFrequency(queries = ["bbb","cc"], words = ["a","aa","aaa","aaaa"]))

