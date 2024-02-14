from typing import List
class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        ans = []
        for word in words:
            cur = ''
            for i in range(len(word)):
                if word[i] == separator:
                    if len(cur) > 0:
                        ans.append(cur)
                    cur = ''
                else:
                    cur += word[i]
            if len(cur)>0:
                ans.append(cur)
        return ans