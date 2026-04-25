class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ret = []
        def combine(i, curList):
            if i == len(nums) or sum(curList) >= target:
                if sum(curList) == target:
                    ret.append(list(curList))
                return;
            
            curList.append(nums[i])
            combine(i, curList)

            curList.pop()
            combine(i + 1, curList)

        combine(0, [])
        return ret

