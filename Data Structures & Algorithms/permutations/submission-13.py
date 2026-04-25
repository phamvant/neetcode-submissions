class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        ret = []
        def backtrack(restList, curList):
            if len(restList) == 0:
                ret.append(list(curList))
                return;

            
            for idx, num in enumerate(restList):
                curList.append(num)
                restList.remove(num)

                backtrack(restList, curList)

                curList.pop()
                restList.insert(idx, num)
        
        backtrack(nums, [])
        return ret