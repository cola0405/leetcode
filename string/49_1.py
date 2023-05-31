from typing import List
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for s in strs:
            tp = tuple(sorted(s))
            if tp in d:
                d[tp].append(s)
            else:
                d[tp] = [s]
        return list(d.values())

print(Solution().groupAnagrams(strs = ["eat", "tea", "tan", "ate", "nat", "bat"]))

