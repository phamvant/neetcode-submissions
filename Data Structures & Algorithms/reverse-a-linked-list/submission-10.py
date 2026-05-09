class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        self.ret = None

        def solve(head, parent):
            if not head:
                return parent
            
            tmp = head.next
            head.next = parent
            return solve(tmp, head)
        
        return solve(head, None)

            
