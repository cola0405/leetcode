class Solution:
    def maximumLength(self, s: str) -> int:
        def fit(k):     # check the length k works or not
            for alpha in seg:
                number = 0
                for l in seg[alpha]:
                    if l >= k:
                        number += (l-k)+1
                if number >= 3:
                    return True
            return False

        seg = {chr(i): [] for i in range(97, 123)}
        i = 0
        while i < len(s):
            cnt = 1
            while i < len(s)-1 and s[i] == s[i+1]:
                cnt += 1
                i += 1

            seg[s[i]].append(cnt)
            i += 1

        low = 1
        high = len(s)
        while low < high:
            mid = (low+high+1)//2
            if fit(mid):
                low = mid
            else:
                high = mid-1
        if low == 1 and not fit(1):
            return -1
        else:
            return low

print(Solution().maximumLength("abcdef"))