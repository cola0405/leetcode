# 贪心，每次放可行的最多的字符
# 需要一个持续有序的数据结构 -- heap

import heapq
class Solution:
    def reorganizeString(self, s: str) -> str:
        # [[0,'a'], [0,'b'], ... ]
        count = [[0, chr(i+97)] for i in range(26)]
        for ch in s:
            count[ord(ch)-97][0] -= 1
        heapq.heapify(count)

        ans = ''
        for i in range(len(s)):
            for j in range(len(count)):
                amount, ch = count[j]
                if (len(ans) != 0 and ans[-1] == ch) or amount == 0:
                    continue
                ans += ch
                count[j][0] += 1
                heapq.heapify(count)
                break
        return ans if len(ans) == len(s) else ""

print(Solution().reorganizeString("aab"))
