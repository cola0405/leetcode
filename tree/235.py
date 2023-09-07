# 利用二叉搜索树的特殊性质

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def get_path(node, target):
            if node is None:
                return None
            if node == target:
                return [node]
            res = get_path(node.left, target)
            if res is not None:
                res.append(node)
                return res

            res = get_path(node.right, target)
            if res is not None:
                res.append(node)
                return res

        path1 = get_path(root, p)
        path2 = get_path(root, q)

        for node in path1:
            if node in path2:
                return node
