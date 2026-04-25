class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        ret = set()
        
        def findset(i, curList):
            if i == len(nums):
                ret.add(tuple(curList))
                return
            
            curList.append(nums[i])
            findset(i + 1, curList)

            curList.pop()
            findset(i + 1, curList)

        findset(0, [])
        return [list(combination) for combination in ret]
