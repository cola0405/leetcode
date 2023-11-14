from typing import List
class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        letters = [set("qwertyuiop"), set("asdfghjkl"), set("zxcvbnm")]

        ans = []
        for word in words:
            s = set(word.lower())
            for line in letters:
                if len(line.union(s)) == len(line):
                    ans.append(word)
                    break
        return ans

print(Solution().findWords(["Hello","Alaska","Dad","Peace"]))

