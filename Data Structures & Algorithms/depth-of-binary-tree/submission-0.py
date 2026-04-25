# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def recursive(self, root: Optional[TreeNode], depth = 0):
        if not root:
            return depth

        newDepthLeft = self.recursive(root.right, depth + 1)
        newDepthRight = self.recursive(root.left, depth + 1)

        return max(newDepthLeft, newDepthRight)


    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.recursive(root) 