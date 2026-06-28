# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = deque([root])
        result = []
        while q:
            n = len(q)
            layer_vals = []
            for i in range(n):
                node = q.popleft()
                if not node: continue
                layer_vals.append(node.val)
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)

            if layer_vals:
                result.append(layer_vals)
        return result
                
        