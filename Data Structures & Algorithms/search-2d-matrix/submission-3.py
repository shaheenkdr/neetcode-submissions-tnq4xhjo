class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        m , n = len(matrix) , len(matrix[0])

        lx, rx = 0, (m * n) - 1

        while lx <= rx:
            mid = (lx + rx) // 2

            val = matrix[mid // n][mid % n]

            if val == target:
                return True

            elif val < target:
                lx = mid + 1
            
            else:
                rx = mid - 1
        
        return False
            
        
        