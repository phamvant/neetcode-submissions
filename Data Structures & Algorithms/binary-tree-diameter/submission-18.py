class Solution:
    def __init__(self):
        self.track = 0

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        leftDepth = self.maxDepth(root.left)
        rightDepth = self.maxDepth(root.right)

        if leftDepth + rightDepth > self.track:
            self.track = leftDepth + rightDepth

        return 1 + max(leftDepth, rightDepth)

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        leftDepth = self.maxDepth(root.left)
        rightDepth = self.maxDepth(root.right)

        if leftDepth + rightDepth > self.track:
            self.track = leftDepth + rightDepth

        return self.track