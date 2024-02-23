class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        from collections import defaultdict
        cnt1 = defaultdict(int)
        for ch in s1:
            cnt1[ch] += 1

        cnt2 = defaultdict(int)
        for i in range(len(s1)):
            cnt2[s2[i]] += 1

        if cnt1 == cnt2:
            return True
        i = 0
        for j in range(len(s1), len(s2)):
            cnt2[s2[j]] += 1
            cnt2[s2[i]] -= 1
            i += 1
            for ch in cnt1:
                if cnt1[ch] != cnt2[ch]:
                    break
            else:
                return True
        return False

print(Solution().checkInclusion(s1 = "ab",s2 = "eidbaooo"))