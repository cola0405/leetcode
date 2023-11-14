class Solution:
    def checkRecord(self, s: str) -> bool:
        for i in range(len(s)-2):
            count = 0
            for j in range(3):
                if s[i+j] == 'L':
                    count += 1
            if count == 3:
                return False
        return s.count('A') < 2