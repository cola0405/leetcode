from typing import Optional, List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        def traversal(layer, node):  # 遍历
            if node is None:
                return
            if visible_nodes[layer] is None:  # 如果当前layer可见节点为None，则更新
                visible_nodes[layer] = node.val
            traversal(layer+1, node.right)  # 优先访问right
            traversal(layer+1, node.left)

        if root is None:
            return []

        visible_nodes = [None]*100
        traversal(1, root)

        ans = []
        for p in range(1,100):
            if visible_nodes[p] is not None:
                ans.append(visible_nodes[p])
            else:
                return ans
