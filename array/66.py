from typing import List
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits.insert(0,0)
        i = len(digits)-1
        digits[i] += 1
        while i>0 and digits[i] == 10:
            digits[i] = 0
            digits[i-1] += 1
            i -= 1

        if digits[0] == 0:
            digits.pop(0)
        return digits

print(Solution().plusOne([9,9,9]))