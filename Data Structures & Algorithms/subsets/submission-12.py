class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        result = []

        def backtrack(start, current_subset):
            # Thêm tập con hiện tại vào kết quả
            result.append(list(current_subset))
            
            for i in range(start, len(nums)):
                # 1. Chọn phần tử nums[i]
                current_subset.append(nums[i])
                
                # 2. Đệ quy để đi sâu hơn
                backtrack(i + 1, current_subset)
                
                # 3. QUAY LUI: Loại bỏ nums[i] để thử phần tử tiếp theo
                current_subset.pop()
                
        backtrack(0, [])
        return result
