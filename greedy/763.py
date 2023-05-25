from typing import List
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        rev_s = s[::-1]
        ans = []
        i = 0
        l = i
        while i<len(s):
            r = len(s)-1-rev_s.index(s[i])  # s[i] in the right end
            while l != r:  # to check if it has farther end
                start = l
                l = r
                for idx in range(start, r):
                    new_r = len(s)-1-rev_s.index(s[idx])
                    r = max(new_r, r)  # get the farthest right end
            ans.append(r-i+1)
            i = r+1  # to next string
            l = i
        return ans

print(Solution().partitionLabels(s="eccbbbbdec"))
