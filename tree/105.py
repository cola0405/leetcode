# 根据前序+中序构造树
# 用好中序的准确划分
# 用好dfs正好对应顺序的前序


from typing import List, Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def build(left, right):  # 根据中序范围+前序配合构造树
            nonlocal i
            # None
            if left>right:  # 想象[1]的用例
                return None
            # leaf
            if left==right:
                i += 1  # 前序正好是dfs的顺序
                return TreeNode(inorder[left])

            cur = preorder[i]
            parent = in_idx[cur]
            node = TreeNode(cur)
            i += 1
            node.left = build(left, parent-1)
            node.right = build(parent+1, right)
            return node

        # build dict for index
        pre_idx = {}
        in_idx = {}
        for i in range(len(preorder)):
            pre_idx[preorder[i]] = i
            in_idx[inorder[i]] = i

        i = 0
        root = build(0, len(preorder)-1)
        return root

print(Solution().buildTree(preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]))