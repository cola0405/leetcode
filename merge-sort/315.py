from typing import List
class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        def merge_sort(l, r):
            if l >= r:
                return 0
            mid = (l+r)//2
            res = merge_sort(l, mid) + merge_sort(mid+1, r)
            nums1 = nums[l:mid+1]
            nums2 = nums[mid+1:r+1]

            i = j = 0
            inx = 0
            for inx in range(l,r+1):
                if inx > 0 and i < len(nums1) and nums[inx-1][0] == nums1[i][0]:
                    nums[inx] = nums[i]
                    ans[nums1[i][1]] += j-1
                    i += 1
                    continue
                if i >= len(nums1) or j >= len(nums2):
                    break
                if nums1[i][0] > nums2[j][0]:
                    nums[inx] = nums2[j]
                    j += 1
                elif nums1[i][0] == nums2[j][0]:
                    nums[inx] = nums2[j]
                    j += 1
                else:
                    nums[inx] = nums1[i]
                    ans[nums1[i][1]] += j
                    i += 1
            while i < len(nums1):
                nums[inx] = nums1[i]
                ans[nums1[i][1]] += len(nums2)
                inx += 1
                i += 1
            while j < len(nums2):
                nums[inx] = nums2[j]
                inx += 1
                j += 1
            return res
        n = len(nums)
        nums = [(nums[i], i) for i in range(n)]
        ans = [0]*n
        merge_sort(0, n-1)
        return ans

print(Solution().countSmaller([-1,-1]))