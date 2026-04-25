class Solution:

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        dummy = ListNode()
        dummy.next = head

        leftNode = dummy
        rightNode = head

        while n > 0:
            rightNode = rightNode.next
            n -= 1

        while rightNode:
            leftNode = leftNode.next
            rightNode = rightNode.next
        
        leftNode.next = leftNode.next.next

        return dummy.next
