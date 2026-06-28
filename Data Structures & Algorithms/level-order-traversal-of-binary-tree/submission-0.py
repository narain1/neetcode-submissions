# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        from collections import deque
        q = deque([root])

        acc = []
        while q:
            layer_len = len(q)
            layer_vals = []
            for i in range(layer_len):
                node = q.popleft()
                if not node: continue
                layer_vals.append(node.val)
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)


            if layer_vals:
                acc.append(layer_vals)
        return acc