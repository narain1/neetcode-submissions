# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        max_depth = 0
        if not root: return 0
        stack = [(root, 1)]
        while stack:
            ptr, depth = stack.pop()
            if ptr.left: stack.append((ptr.left, depth + 1))
            if ptr.right: stack.append((ptr.right, depth + 1))
            max_depth = max(max_depth, depth)
        return max_depth
