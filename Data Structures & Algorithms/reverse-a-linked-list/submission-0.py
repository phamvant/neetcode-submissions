
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prevNode = None
        nextNode = None
        currentNode = head

        while currentNode:
            nextNode = currentNode.next

            currentNode.next = prevNode
            prevNode = currentNode

            currentNode = nextNode

            
        return prevNode