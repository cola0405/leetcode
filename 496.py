from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = [nums2[-1]]
        d = {nums2[-1]: -1}
        for i in range(len(nums2)-1)[::-1]:
            while len(stack)>0 and stack[-1] < nums2[i]:
                stack.pop()
            d[nums2[i]] = -1 if len(stack)==0 else stack[-1]
            stack.append(nums2[i])
        ans = []
        for num in nums1:
            ans.append(d[num])
        return ans

print(Solution().nextGreaterElement(nums1 = [4,1,2], nums2 = [1,3,4,2]))
        
        