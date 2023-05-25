class Solution:
    def balancedStringSplit(self, s: str) -> int:
        count = {'R':0, 'L':0}
        ans = 0
        for ch in s:
            count[ch] += 1
            if count['L']==count['R']:
                count['L'] = 0
                count['R'] = 0
                ans += 1
        return ans

print(Solution().balancedStringSplit(s = "RLRRRLLRLL"))