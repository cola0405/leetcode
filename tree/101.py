from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 一般情况下，完全二叉树才适用数组表示法
# 但是数组表示法有它独特的用处 -- 能够表示二叉树的结构特征，我们甚至可以用来判断是否镜面对称
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if (root.left is None and root.right is not None)\
                or (root.left is not None and root.right is None):
            return False

        from collections import deque
        left = deque([root.left])
        left_nodes = []
        while len(left)>0:
            node = left.popleft()
            if node is None:
                left_nodes.append(None)
                continue
            left_nodes.append(node.val)
            left.append(node.right)  # 左边先放right，再放left -- 为了镜像对称
            left.append(node.left)

        right = deque([root.right])
        right_nodes = []
        while len(right) > 0:
            node = right.popleft()
            if node is None:
                right_nodes.append(None)
                continue
            right_nodes.append(node.val)
            right.append(node.left)
            right.append(node.right)

        return left_nodes == right_nodes

print(Solution().isSymmetric())


