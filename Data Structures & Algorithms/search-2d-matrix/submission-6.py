class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        m, n = len(matrix), len(matrix[0])

        lx, rx = 0 , (m * n) - 1

        while lx <= rx:

            mid = (lx + rx) // 2

            r = mid // n
            c = mid % n

            if matrix[r][c] == target:
                return True
            
            elif matrix[r][c] < target:
                lx = mid + 1
            
            else:
                rx = mid - 1
        
        return False
        