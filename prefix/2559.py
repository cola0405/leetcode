from typing import List
class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels = 'aeiou'
        pre = [0]
        for word in words:
            if word[0] in vowels and word[-1] in vowels:
                pre.append(pre[-1]+1)
            else:
                pre.append(pre[-1])

        ans = []
        for l,r in queries:
            ans.append(pre[r+1]-pre[l])
        return ans

print(Solution().vowelStrings(words = ["aba","bcb","ece","aa","e"], queries = [[0,2],[1,4],[1,1]]))