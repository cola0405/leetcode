class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        i = 0
        j = 0
        while j<len(typed):
            if i<len(name) and name[i] == typed[j]:
                i += 1
                j += 1
            elif i>0 and typed[j] == name[i-1]:
                while j<len(typed):
                    if typed[j] != name[i-1]:
                        break
                    j += 1
            else:
                return False
        return True if i == len(name) else False

print(Solution().isLongPressedName("saeed",
"ssaaedd"))