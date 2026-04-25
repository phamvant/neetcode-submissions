
class Solution:

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        ROWS = len(matrix)
        COLS = len(matrix[0])

        l, r = 0, COLS * ROWS - 1

        while l <= r:
            m = l + (r - l) // 2
            col = m % COLS
            row = m // COLS

            middleVal = matrix[row][col]


            if middleVal > target:
                r = m - 1
            elif middleVal < target:
                l = m + 1
            else:
                return True
        
        return False
        
