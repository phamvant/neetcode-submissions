# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def dfs(cur, prev, curMax):
            if not cur:
                return 0

            nextMax = max(curMax, cur.val)
            isGood = 1 if (cur.val >= prev.val and cur.val >= curMax) else 0
            ret1 = dfs(cur.left, cur, nextMax)
            ret2 = dfs(cur.right, cur, nextMax)
            print(cur.val, prev.val)
            print("g", isGood)
            
            return ret1 + ret2 + isGood
    
        return dfs(root, root, root.val)
            
