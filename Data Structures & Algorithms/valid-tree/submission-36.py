class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        hashMap = {i: [] for i in range(n)}
        visited = set()

        for cur, nex in edges:
            hashMap[cur].append(nex)
            hashMap[nex].append(cur)

        print(hashMap)
        if len(edges) != n - 1:
            return False

        def dfs(node, par):
            if node in visited:
                return False
            
            visited.add(node)

            for j in hashMap[node]:
                if j == par:
                    continue
                if not dfs(j, node):
                    return False

            return True
        
        for i in range(n):
            visited = set()
            if dfs(i, i) and len(visited) == n:
                return True

        return False
