class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        ans = []
        i = j = 0
        while i < len(word1) and j < len(word2):
            if word1[i:] >= word2[j:]:
                ans.append(word1[i])
                i += 1
            else:
                ans.append(word2[j])
                j += 1
        while i < len(word1):
            ans.append(word1[i])
            i += 1
        while j < len(word2):
            ans.append(word2[j])
            j += 1
        return ''.join(ans)

print(Solution().largestMerge(word1 = "abcabc", word2 = "abdcaba"))