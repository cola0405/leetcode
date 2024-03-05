# optimize two pointers
class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        ans = []
        i = j = 0
        while i < len(word1) or j < len(word2):
            if i < len(word1) and word1[i:] >= word2[j:]:
                ans.append(word1[i])
                i += 1
            else:
                ans.append(word2[j])
                j += 1
        return ''.join(ans)

print(Solution().largestMerge(word1 = "abcabc", word2 = "abdcaba"))