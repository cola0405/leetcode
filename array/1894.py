from typing import List
class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        remain = k%sum(chalk)
        for i in range(len(chalk)):
            if chalk[i] > remain:
                return i
            remain -= chalk[i]
