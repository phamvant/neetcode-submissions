# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        stack = [(root, 0)]
        ret = []

        while len(stack):
            curNode, curDepth = stack.pop()

            if not curNode:
                continue

            if len(ret) == curDepth:
                ret.append(curNode.val)
            
            stack.append((curNode.left, curDepth + 1))
            stack.append((curNode.right, curDepth + 1))

        return ret
            
