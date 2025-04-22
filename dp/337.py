# Definition for a binary tree node.
from functools import cache
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        @cache          # 会有节点被重复递归到，因为可能从上一个节点来，也可能从上上个节点来
        def dfs(x):
            if x is None:
                return 0
            res1 = dfs(x.left) + dfs(x.right)       # 不抢当前节点
            res2 = 0                                # 抢当前节点
            if x.left:
                res2 += dfs(x.left.left) + dfs(x.left.right)
            if x.right:
                res2 += dfs(x.right.left) + dfs(x.right.right)
            return max(res1, x.val + res2)

        return dfs(root)