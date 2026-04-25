class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        ret = []
        
        def findset(i, curList):
            if i == len(nums):
                ret.append(list(curList))
                return
            
            curList.append(nums[i])
            findset(i + 1, curList)

            curList.pop()
            findset(i + 1, curList)

        findset(0, [])
        print(ret)
        return ret
