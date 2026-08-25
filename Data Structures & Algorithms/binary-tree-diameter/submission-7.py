# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0

        def dfs(tree):
            if not tree: return 0
            left_max = dfs(tree.left)
            right_max = dfs(tree.right)

            self.diameter = max(self.diameter, left_max + right_max)
            return max(left_max, right_max) + 1

        dfs(root)
        return self.diameter
