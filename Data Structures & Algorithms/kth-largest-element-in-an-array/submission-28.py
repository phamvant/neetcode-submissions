import random

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Convert k to the index in a sorted array (0-indexed)
        target = len(nums) - k
        l, r = 0, len(nums) - 1
        
        while l <= r:
            # Randomize pivot to avoid O(n^2) worst case
            pivot_idx = random.randint(l, r)
            nums[pivot_idx], nums[r] = nums[r], nums[pivot_idx]
            
            # Standard Partition logic
            pivot = nums[r]
            p = l
            for i in range(l, r):
                if nums[i] <= pivot:
                    nums[p], nums[i] = nums[i], nums[p]
                    p += 1
            nums[p], nums[r] = nums[r], nums[p]
            
            # Binary search-like logic
            if p > target:
                r = p - 1
            elif p < target:
                l = p + 1
            else:
                return nums[p]