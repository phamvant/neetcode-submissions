class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        hashMap = {i: [] for i in range(numCourses)}
        for crs, need in prerequisites:
            hashMap[crs].append(need)
        visited = set()
        ret = []

        def dfs(i):
            if i in visited:
                return False
            
            visited.add(i)

            for crs in hashMap[i]:
                if not dfs(crs):
                    return False

            if i not in ret:
                ret.append(i)

            if len(hashMap[i]) == 0:
                if i not in ret:
                    ret.append(i)
                visited.remove(i)
                return True

            visited.remove(i)
        
            return True

        for i in range(numCourses):
            if dfs(i) and len(ret) == numCourses:
                return ret
        
        return []