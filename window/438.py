# 滑动窗口 统计问题

from typing import List
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        from collections import defaultdict, Counter
        n, m = len(s), len(p)
        count1 = Counter(p)
        count2 = defaultdict(int)

        ans = []
        for i in range(n):
            count2[s[i]] += 1
            if i < m-1:  # 恰好为m-1时，是需要做一次检查的
                continue

            if i >= m:  # 维护window
                count2[s[i-m]] -= 1

            for ch in count1:  # check
                if count1[ch] != count2[ch]:
                    break
            else:
                ans.append(i-m+1)
        return ans

print(Solution().findAnagrams(s = "cbaebabacd", p = "abc"))


