from typing import List
class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        arr = []
        while len(nums) > 0:
            min_num1 = min(nums)
            nums.remove(min_num1)
            if len(nums) == 0:
                arr.append(min_num1)
                break
            min_num2 = min(nums)
            nums.remove(min_num2)

            arr.append(min_num2)
            arr.append(min_num1)
        return arr
