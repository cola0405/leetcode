from typing import List
class Solution:
    def findLUSlength(self, strs: List[str]) -> int:
        max_len = 0
        for s in strs:
            max_len = max(max_len, len(s))
        return max_len if len(set(strs)) != 1 else -1

print(Solution().findLUSlength(["aba","cdc","eae"]))

