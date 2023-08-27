from typing import List
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        from collections import defaultdict
        count = defaultdict(int)
        for i in range(len(s)-9):
            sub = s[i:i+10]
            count[sub] += 1

        ans = []
        for sub, amount in count.items():
            if amount > 1:
                ans.append(sub)
        return ans

print(Solution().findRepeatedDnaSequences("AAAAAAAAAAA"))