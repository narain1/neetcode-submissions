# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not p or not q or not root:
            return None
        parent_val = root.val
        p_val = p.val
        q_val = q.val

        if parent_val < p_val and parent_val < q_val:
            return self.lowestCommonAncestor(root.right, p, q)
        elif parent_val > p_val and parent_val > q_val:
            return self.lowestCommonAncestor(root.left, p, q)
        else:
            return root
        