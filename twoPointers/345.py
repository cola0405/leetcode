class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        i = 0
        j = len(s)-1

        target = 'aeiouAEIOU'
        while i<j:
            while i<=j and s[i] not in target:
                i += 1
            while j>=i and s[j] not in target:
                j -= 1

            if i<j:
                s[i],s[j] = s[j],s[i]
            i += 1
            j -= 1
        return ''.join(s)

print(Solution().reverseVowels("leetcode"))