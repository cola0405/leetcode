class Solution:
    def minimumScore(self, s: str, t: str) -> int:
        from collections import defaultdict, Counter
        def is_sub(cnt1):
            for c in cnt1:
                if cnt1[c] > cnt[c]:
                    return False
            return True

        def fit(n):
            cnt1 = Counter(t)
            for i in range(n):
                cnt1[t[i]] -= 1
            if is_sub(cnt1):
                return True
            i = 0
            for j in range(n, len(t)):
                cnt1[t[i]] += 1
                cnt1[t[j]] -= 1
                i += 1
                if is_sub(cnt1):
                    return True
            return False

        cnt = Counter(s)
        low = 0
        high = len(t)
        while low < high:
            mid = (low+high)//2
            if fit(mid):
                high = mid
            else:
                low = mid+1
        return low

print(Solution().minimumScore(s = "abecdebe", t = "eaebceae"))