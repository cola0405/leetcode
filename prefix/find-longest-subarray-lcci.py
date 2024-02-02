# longest interval with the same endpoints in diff

# we can count the diff between number and alpha
# then find out the longest interval that the two endpoints are the same -- like 1 2 3 2 1 -- (1,1)
# it represent that the number and alpha between two endpoints make balanced

# see also 525.py
from typing import List
class Solution:
    def findLongestSubarray(self, array: List[str]) -> List[str]:
        diff = [0]
        for ch in array:
            if 'a' <= ch <= 'z' or 'A' <= ch <= 'Z':
                diff.append(diff[-1]+1)
            else:
                diff.append(diff[-1]-1)

        # find the last index with the same diff[i]
        inx = dict()
        for i in range(len(diff))[::-1]:
            if diff[i] not in inx:
                inx[diff[i]] = i

        left = 0    # represent the answer start from 0 first
        for i in range(1,len(diff)):
            if inx[diff[i]] - i > inx[diff[left]] - left:
                left = i
        # there do have the offset between diff and array -- it should be range(left+1,inx[diff[left]]+1) in theory
        return [array[i] for i in range(left, inx[diff[left]])]

print(Solution().findLongestSubarray(["A","1","B","C","D","2","3","4","E","5","F","G","6","7","H","I","J","K","L","M"]))


