class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        diff = []
        for i in range(len(s)):
            if s[i] != goal[i]:
                diff.append(i)
                if len(diff) > 2:
                    return False
        if len(diff) != 0 or len(set(s))!=len(s):
            return True
        return False

print(Solution().buddyStrings(s = "aa", goal = "aa"))