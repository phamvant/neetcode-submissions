class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        cur = head

        if not (list1 and list2):
            cur.next = list1 if not list2 else list2

        while list1 and list2:
            if list1.val < list2.val:
                cur.next = list1
                list1 = list1.next
            else:
                cur.next = list2
                list2 = list2.next
            
            cur = cur.next
            print(cur.val)
            
            if not (list1 and list2):
                cur.next = list1 if not list2 else list2
            
        return head.next