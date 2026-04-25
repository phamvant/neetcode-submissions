class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        middle = target // 2
        l, r = 0, len(numbers) - 1

        while(l < r):
            if (numbers[l] + numbers[r] < target):
                l += 1
            if(numbers[r] == target - numbers[l]):
                break;
            if (numbers[r] + numbers[l] > target):
                r -= 1
            if(numbers[r] == target - numbers[l]):
                break;
            if (numbers[r] + numbers[l] == target):
                r -= 1
                l += 1
                break;
            
        return [l + 1, r + 1]