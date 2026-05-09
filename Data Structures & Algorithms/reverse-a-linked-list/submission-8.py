class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        self.ret = None

        def solve(head, parent):
            if not head:
                self.ret = parent
                return
            
            solve(head.next, head)
            head.next = parent
        
        solve(head, None)
        
        return self.ret

            
