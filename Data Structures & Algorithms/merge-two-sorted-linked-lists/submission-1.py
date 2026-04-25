class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        headNode = tmpNode = ListNode()

        while list1 and list2:
            if list1.val <= list2.val:
                tmpNode.next = list1
                list1 = list1.next
            else:
                tmpNode.next = list2
                list2 = list2.next
            tmpNode = tmpNode.next

        tmpNode.next = list1 or list2

        return headNode.next
