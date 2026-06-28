# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_sum = float("-inf")
        def dfs(root):
            nonlocal max_sum
            if not root: return 0
            left_max = max(0, dfs(root.left))
            right_max = max(0, dfs(root.right))
            max_sum = max(max_sum, left_max + right_max + root.val)
            return max(left_max, right_max) + root.val
        
        dfs(root)
        return max_sum

        