
class Solution:

    def searchCol(self, matrix, target) -> int:
        row = len(matrix[0]) - 1
        col = len(matrix) - 1
        t, b = 0, col
        middle = t + (b - t) // 2

        while t <= b:
            middle = t + (b - t) // 2
            middleVal = matrix[middle][0]

            if b <= t:
                return b

            if middleVal > target:
                b = middle - 1
            elif middleVal < target:
                if matrix[middle][row] >= target:
                    return middle
                t = middle + 1
            else:
                return middle

            if b <= t:
                return b




    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        colIdx = self.searchCol(matrix, target)
        
        l, r = 0, len(matrix[0]) - 1
        middle = l + (r - l) // 2
        
        while l <= r:
            middle = l + (r - l) // 2
            middleVal = matrix[colIdx][middle]

            if middleVal == target:
                return True

            if middleVal < target:
                l = middle + 1
            elif middleVal > target:
                r = middle - 1
            else:
                return False
        
        return False
        