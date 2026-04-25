class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0, 0

        leftDepth, leftDiameter = self.maxDepth(root.left)
        rightDepth, rightDiameter = self.maxDepth(root.right)

        return 1 + max(leftDepth, rightDepth), max(leftDiameter, rightDiameter, (leftDepth + rightDepth))

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        depth, diameter = self.maxDepth(root)
        return diameter
