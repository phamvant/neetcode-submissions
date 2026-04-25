"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:

    def __init__(self):
        self.hashMap = {}


    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        newNode = Node(head.val)
        self.hashMap[head] = newNode
        nextNode = self.copyRandomList(head.next)
        newNode.next = nextNode
        newNode.random = self.hashMap.get(head.random)

        return newNode
            