from typing import List
class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        from collections import defaultdict, Counter
        max_count = defaultdict(int)
        for word in words2:
            count = defaultdict(int)
            for ch in word:
                count[ch] += 1
            for ch in count:
                max_count[ch] = max(max_count[ch], count[ch])

        ans = []
        for word in words1:
            counter = Counter(word)
            for ch in max_count:
                if counter[ch] < max_count[ch]:
                    break
            else:
                ans.append(word)
        return ans

print(Solution().wordSubsets(words1 = ["amazon","apple","facebook","google","leetcode"], words2 = ["e","o"]))

