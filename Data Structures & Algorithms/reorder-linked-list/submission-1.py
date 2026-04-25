class Solution:
    def moveNode(self, root: Optional[ListNode], cur: Optional[ListNode]):
        if not cur:
            return root
        
        root = self.moveNode(root, cur.next)

        if not root:
            return None
        
        if root == cur or root.next == cur:
            cur.next = None
            return None

        tmp = root.next
        root.next = cur
        cur.next = tmp
      
        return tmp

    def reorderList(self, head: Optional[ListNode]):
        root = head
        self.moveNode(root, head)