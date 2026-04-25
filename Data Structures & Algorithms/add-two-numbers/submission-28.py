# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def add(self, l1, l2, carry):
        if not (l1 or l2):
            if not carry:
                return None

        sum = (l1.val if l1 else 0) + (l2.val if l2 else 0) + carry
        newNode = self.add(l1.next if l1 else None, l2.next if l2 else None, 1 if sum > 9 else 0)

        head = ListNode(sum % 10)
        head.next = newNode

        return head
        
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        return self.add(l1, l2, 0)
        