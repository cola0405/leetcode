# two pointers
from collections import Counter
class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        cnt = Counter(s)
        cur = tmp = 122
        ans = []
        cur_size = 0
        while cur >= 97 and tmp >= 97:      # two pointers + one loop step by step
            if cnt[chr(cur)] == 0:
                cur -= 1
                cur_size = 0
            elif cur_size == repeatLimit:
                if cnt[chr(tmp)] != 0 and tmp != cur:
                    ans.append(chr(tmp))    # insert others to reset
                    cnt[chr(tmp)] -= 1
                    cur_size = 0
                else:
                    tmp -= 1
            else:
                ans.append(chr(cur))
                cnt[chr(cur)] -= 1
                cur_size += 1       # watch on the length
        return ''.join(ans)



print(Solution().repeatLimitedString(s = "aababab", repeatLimit = 2))
