class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        ret = []
        def backtrack(restList, curList):
            if len(restList) == 0:
                ret.append(list(curList))
                return;

            
            for num in restList:
                tmpCurList = list(curList)
                tmpCurList.append(num)

                tmpRestList = list(restList)
                tmpRestList.remove(num)
                backtrack(tmpRestList, tmpCurList)
        
        backtrack(nums, [])
        return ret