from typing import List
class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        n = len(skill)
        skill.sort()
        target = skill[0] + skill[-1]
        ans = 0
        for i in range(n//2):
            if skill[i] + skill[-i-1] != target:
                return -1
            ans += skill[i]*skill[-i-1]
        return ans