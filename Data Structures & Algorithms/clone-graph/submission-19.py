from collections import deque

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        hashMap = {}

        def bfs():
            q = deque([node])
            newHead = None

            while len(q) > 0:
                current = q.popleft()
                if not current:
                    return newHead

                if not hashMap.get(current, 0):
                    hashMap[current] = Node(current.val)
                tmpHead = hashMap.get(current)
                
                if not newHead:
                    newHead = tmpHead
                
                for n in current.neighbors:
                    if not hashMap.get(n, 0):
                        q.append(n)
                        hashMap[n] = Node(n.val)

                    tmpHead.neighbors.append(hashMap[n])

            return newHead

        return bfs()
