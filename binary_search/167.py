from typing import List
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        for i in range(n-1):
            num = target - numbers[i]
            low = i+1
            high = n-1
            while low <= high:
                mid = (low+high)//2
                if numbers[mid] == num:
                    return [i+1, mid+1]
                elif numbers[mid] > num:
                    high = mid-1
                else:
                    low = mid+1

