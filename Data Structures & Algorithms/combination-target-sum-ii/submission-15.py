class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        ret = set()
        nums.sort()

        def combine(i, curList):
            if i == len(nums) or sum(curList) >= target:
                if sum(curList) == target:
                    ret.add(tuple(curList))
                return;
            
            curList.append(nums[i])
            combine(i + 1, curList)

            curList.pop()
            while i < len(nums) - 1 and nums[i] == nums[i + 1]:
                i += 1
            combine(i + 1, curList)

        combine(0, [])
        return [list(combination) for combination in ret]

