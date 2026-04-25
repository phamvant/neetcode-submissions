# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def height(self, root: Optional[TreeNode]):
        if not root:
            return 0, True

        leftHeight, isFalseLeft = self.height(root.left)
        rightHeight, isFalseRight = self.height(root.right)

        if not (isFalseLeft and isFalseRight):
            return 0, False

        return 1 + max(leftHeight, rightHeight), abs(leftHeight - rightHeight) < 2

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        height, ret = self.height(root)
        return ret
        
        