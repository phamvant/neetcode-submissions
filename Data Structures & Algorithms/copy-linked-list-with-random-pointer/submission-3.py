"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def createNodes(self, hashMap, head):
        if not head:
            return None

        newNode = Node(head.val)
        hashMap[head] = newNode
        nextNode = self.createNodes(hashMap, head.next)
        newNode.next = nextNode
        newNode.random = hashMap.get(head.random)

        return newNode

    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        hashMap = {}

        newHead = self.createNodes(hashMap, head)
        return newHead
            