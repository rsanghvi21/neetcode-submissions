class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row_len = len(matrix)
        col_len = len(matrix[0])
        l, r = 0, row_len * col_len - 1
        
        while l <= r:
            mid = l + (r - l) // 2
            val = matrix[mid // col_len][mid % col_len]
            
            if target > val:
                l = mid + 1
            elif target < val:
                r = mid - 1
            else:
                return True
                
        return False