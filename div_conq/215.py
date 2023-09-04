# 分治

# 只是求第k大的数，不需要让其他元素有序
# 想到快排，只要左右两边能分好就行了

# 分治和dfs搜索是有本质区别的
# 分治核心就是对数据进行拆分，然后再进入目标段做进一步处理


from typing import List
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        import random
        def quick_sort(lst, pos):
            pivot = random.choice(lst)
            large = []
            small = []
            equal = []
            for num in lst:
                if num > pivot:
                    large.append(num)
                elif num < pivot:
                    small.append(num)
                else:
                    equal.append(num)

            if len(large)>=pos:
                return quick_sort(large, pos)
            elif len(large)+len(equal)<pos:
                return quick_sort(small, pos-len(large)-len(equal))
            else:
                return pivot

        return quick_sort(nums, k)

print(Solution().findKthLargest([3,2,1,5,6,4],2))




