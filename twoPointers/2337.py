class Solution:
    def canChange(self, start: str, target: str) -> bool:
        if start.replace('_', '') != target.replace('_', ''):
            return False
        j = 0
        for i in range(len(start)):
            if start[i] == '_':     # skip the part
                continue
            while j < len(target) and target[j] == '_':
                j += 1
            if start[i] == 'L' and i < j:
                return False
            elif start[i] == 'R' and i > j:
                return False
            j += 1
        return True