from typing import List
class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        positive = []
        negative = []
        for num in nums:
            if num > 0:
                positive.append(num)
            else:
                negative.append(num)
        ans = []
        for i in range(len(positive)):
            ans.append(positive[i])
            ans.append(negative[i])
        return ans