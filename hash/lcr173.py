from typing import List
class Solution:
    def takeAttendance(self, records: List[int]) -> int:
        s = set(records)
        for num in range(len(records)+1):
            if num not in s:
                return num