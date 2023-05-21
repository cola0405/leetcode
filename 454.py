from typing import List


class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        s1 = {}
        for a in nums1:
            for b in nums2:
                res = a+b
                if res not in s1:
                    s1[res] = 1
                else:
                    s1[res] += 1

        s2 = {}
        for c in nums3:
            for d in nums4:
                res = c + d
                if res not in s2:
                    s2[res] = 1
                else:
                    s2[res] += 1
        ans = 0
        for num in s1:
            if -num in s2:
                ans += s1[num]*s2[-num]
        return ans

print(Solution().fourSumCount(nums1 = [1,2], nums2 = [-2,-1], nums3 = [-1,2], nums4 = [0,2]))


# import profile
# profile.run('main()')