class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False

        hashMap = {i: [] for i in range(n)}
        for node, nex in edges:
            hashMap[node].append(nex)
            hashMap[nex].append(node)

        visited = set()

        def dfs(start, prev):
            if start in visited:
                return False
            
            visited.add(start)
            for i in hashMap[start]:
                if i == prev:
                    continue
                if not dfs(i, start):
                    return False

            return True

        return dfs(0, -1) and len(visited) == n
