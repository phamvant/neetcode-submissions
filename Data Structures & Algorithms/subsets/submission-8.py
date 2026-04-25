class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        ret = []
        cart = []
        
        def subset(i):
            if i >= len(nums):
                ret.append(cart.copy())
                return;
            
            cart.append(nums[i])
            subset(i + 1)

            cart.pop()
            subset(i + 1)

        subset(0)
        
        return ret
            

