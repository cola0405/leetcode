from typing import List
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        ordered_s = [0]*len(strs)
        i = 0
        for s in map(sorted, strs):
            ordered_s[i] = (s, i)
            i += 1
        ordered_s.sort(key=lambda item:item[0])

        group = []
        for i in range(len(strs)-1):
            s, idx = ordered_s[i]
            group.append(strs[idx])
            if ordered_s[i][0] != ordered_s[i+1][0]:
                res.append(group)
                group = []
        # tail
        if len(group) == 0:
            res.append([strs[ordered_s[-1][1]]])
        else:
            group.append(strs[ordered_s[-1][1]])
            res.append(group)
        return res

print(Solution().groupAnagrams(strs = ["eat", "tea", "tan", "ate", "nat", "bat"]))

