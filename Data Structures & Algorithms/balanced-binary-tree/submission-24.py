# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        stack = [root]
        mp = {}

        while len(stack) > 0:
            current = stack[-1]

            if current.left and current.left not in mp:
                stack.append(current.left)
            elif current.right and current.right not in mp:
                stack.append(current.right)
            else:
                stack.pop()
                
                leftHeight = mp[current.left] if current.left else 0
                rightHeight = mp[current.right] if current.right else 0

                mp[current] = 1 + max(leftHeight, rightHeight)
                if abs(leftHeight - rightHeight) > 1:
                    return False
        
        return True

            
        
        