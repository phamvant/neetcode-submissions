class Solution:


    def removeRecur(self, head: Optional[ListNode], n: int):
        if not head:
            return 0

        idxFromHead = self.removeRecur(head.next, n)

        if idxFromHead == n:
            head.next = head.next.next

        return idxFromHead + 1
    
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        tmp = ListNode()
        tmp.next = head

        self.removeRecur(tmp, n)

        return tmp.next