# 暴力双指针超时
# 利用map优化匹配时的指针右移

# map 的结构如下：
# s = 'abcabc'
# {a:[0,3], b:[1,4], c[2,5]}
# 然后用二分upper下一个的索引
# 如果全部都顺利，则表示是子序列
# 如果check时，有next在cur左边的，那表示未满足子序列的条件

from collections import defaultdict
from typing import List
class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        def upper(lst, target):
            if len(lst) == 0:
                return -1

            low = 0
            high = len(lst)-1
            while low < high:
                mid = (low+high)//2
                if lst[mid] > target:
                    high = mid  # upper bound
                else:
                    low = mid+1
            return lst[low]

        def sub(word):
            if len(nxt[word[0]]) == 0:
                return False

            cur = nxt[word[0]][0]
            for i in range(1,len(word)):  # check 剩下的 n-1个字母
                idx = upper(nxt[word[i]], cur)
                if idx <= cur:  # 如果 next 在 cur 左边
                    return False
                cur = idx
            return True


        # build map
        nxt = defaultdict(list)
        for i in range(len(s)):
            nxt[s[i]].append(i)

        ans = 0
        for w in words:
            if sub(w):
                ans += 1
        return ans

print(Solution().numMatchingSubseq("abcabc", ['abaa']))