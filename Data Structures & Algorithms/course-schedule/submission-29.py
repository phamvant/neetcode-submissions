class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        hashMap = {i: [] for i in range(numCourses)}
        for need, crs in prerequisites:
            hashMap[crs].append(need)
        visited = set()

        def dfs(i):
            if i in visited:
                return False

            if len(hashMap.get(i, [])) == 0:
                return True

            visited.add(i)
            for pre in hashMap[i]:
                if not (dfs(pre)):
                    return False
            visited.remove(i)

            return True

        for i in range(numCourses):
            if not (dfs(i)):
                return False

        return True