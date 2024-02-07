from typing import List
class Solution:
    def trainingPlan(self, actions: List[int]) -> List[int]:
        odd = []
        even = []
        for num in actions:
            if num%2 == 0:
                even.append(num)
            else:
                odd.append(num)
        return odd + even