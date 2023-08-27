from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 并行比较dfs
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def parallel_comp(left, right):
            if left is None and right is None:
                return True
            if left is None or right is None or left.val != right.val:
                return False
            return parallel_comp(left.right, right.left) and parallel_comp(left.left, right.right)
        return parallel_comp(root.left, root.right)



