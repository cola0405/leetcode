from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        i = len(digits)-1
        digits[i] += 1
        if digits[i] > 9:
            while i-1 >= 0 and digits[i-1]+1 > 9:
                digits[i] = 0
                i -= 1
            if i > 0:
                digits[i] = 0
                digits[i-1] += 1
            if i == 0:
                if digits[0]+1 > 9:
                    digits[0] = 0
                    digits.insert(0, 1)
                else:
                    digits[0] += 1
        return digits