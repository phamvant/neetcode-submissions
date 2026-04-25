# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p, q) -> bool:
        stack = [(p, q)]

        while len(stack) > 0:
            
            curP, curQ = stack.pop()
            
            if not curP and not curQ:
                continue

            if not (curP and curQ) or (curP.val != curQ.val):
                return False

            stack.append((curP.left, curQ.left))
            stack.append((curP.right, curQ.right))
            
        return True
