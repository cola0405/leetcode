# 二叉搜索树的二分打开方式


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        while root:
            if root.val > max(p.val, q.val):
                root = root.left
            elif root.val < min(p.val, q.val):
                root = root.right
            else:  # p和q之间的数就一定是答案，不会有多个答案 -- 在二叉搜索树结构限制下
                return root
