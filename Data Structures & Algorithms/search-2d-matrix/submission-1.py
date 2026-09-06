class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row_len = len(matrix)
        col_len = len(matrix[0])
        l, r = 0, row_len * col_len - 1

        while l <= r:
            mid = l + (r - l) // 2
            row = mid // col_len
            col = mid % col_len
            val = matrix[row][col]
            if val < target:
                l = mid + 1
            elif val > target:
                r = mid - 1
            else:
                return True
        return False
        
        