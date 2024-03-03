from typing import List
class Solution:
    def compress(self, chars: List[str]) -> int:
        n = len(chars)
        ans = []
        i = 0
        while i < n:
            j = i
            while j+1 < n and chars[j] == chars[j+1]:
                j += 1
            ans.append(chars[i])
            cnt = j-i+1
            if cnt > 1:
                ans += list(str(cnt))
            i = j+1
        for i in range(len(ans)):
            chars[i] = ans[i]
        return len(ans)

print(Solution().compress(["a"]))

