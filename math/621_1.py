# math
# find the most common element X
# there must be n elements between every X
# so -- (max_cnt-1)*n + max_cnt
# because there may do have serval common elements
# so +count(max_cnt) at the end

from typing import List
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        from collections import Counter
        cnt = Counter(tasks)
        max_cnt = max(cnt.values())
        ans = (max_cnt-1)*n + max_cnt + list(cnt.values()).count(max_cnt)-1
        return max(ans, len(tasks))

print(Solution().leastInterval(["A","A","A","A","A","A","B","C","D","E","F","G"], n = 1))


