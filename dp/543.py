# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans = 0
        def dfs(x):
            nonlocal ans
            if x is None:
                return -1
            l = dfs(x.left) + 1
            r = dfs(x.right) + 1
            ans = max(ans, l+r)
            return max(l, r)

        dfs(root)
        return ans
