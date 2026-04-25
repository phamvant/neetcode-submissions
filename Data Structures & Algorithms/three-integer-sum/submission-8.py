class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        count = {}
        res = []

        for i in range(len(nums)):
            count[nums[i]] = 1 + count.get(nums[i], 0)
        
        for i in range(len(nums) - 1):
            count[nums[i]] -= 1
            
            if i and nums[i] == nums[i - 1]:
                continue

            for j in range(i + 1, len(nums) - 1):
                count[nums[j]] -= 1

                if j - 1 > i and nums[j] == nums[j - 1]:
                    continue

                target = -(nums[i] + nums[j])

                if count.get(target, 0) > 0:
                    res.append([nums[i], nums[j], target])

            for j in range(i + 1, len(nums) - 1):
                count[nums[j]] += 1

        return res


