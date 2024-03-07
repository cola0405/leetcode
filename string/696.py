# seg
class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        n = len(s)
        seg = []
        i = 0
        while i < n:
            j = i+1
            while j < n and s[j] == s[j-1]:
                j += 1
            seg.append(j-i)
            i = j
        ans = 0
        for i in range(len(seg)-1):
            ans += min(seg[i],seg[i+1])
        return ans

print(Solution().countBinarySubstrings("00110011"))
                    
