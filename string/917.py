class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        chars = []
        for ch in s:
            if 'a' <= ch <= 'z' or 'A' <= ch <= 'Z':
                chars.append(ch)
        ans = []
        for i in range(len(s)):
            if 'a' <= s[i] <= 'z' or 'A' <= s[i] <= 'Z':
                ans.append(chars.pop())
            else:
                ans.append(s[i])
        return ''.join(ans)

print(Solution().reverseOnlyLetters("a-bC-dEf-ghIj"))