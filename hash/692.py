from typing import List
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        from collections import Counter
        count = [(word, amount) for word, amount in Counter(words).items()]
        count.sort(key=lambda item: item[1], reverse=True)

        ans = []
        i = 0
        while len(ans) < k:
            temp = []
            while len(temp) == 0 or (i<len(count) and temp[-1][1] == count[i][1]):
                temp.append(count[i])
                i += 1
            temp.sort(key=lambda item: item[0])
            ans += temp[:k-len(ans)]
        return [item[0] for item in ans]


print(Solution().topKFrequent(words = ["i","love","leetcode","i","love","coding"], k = 3))
