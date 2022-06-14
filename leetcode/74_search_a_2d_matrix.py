class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])
        
        top, bot = 0, ROWS - 1
        
        while top <= bot:
            mid_row = (top + bot) // 2
            if target > matrix[mid_row][-1]:
                top = mid_row + 1
            elif target < matrix[mid_row][0]:
                bot = mid_row - 1
            else:
                break

        if not (top <= bot):
            return False
        
        row = (top + bot ) // 2
        
        l, r = 0, COLS -1
        while l <= r:
            midle_col = (r + l) // 2
            if target > matrix[row][midle_col]:
                l = midle_col + 1
            elif target < matrix[row][midle_col]:
                r = midle_col - 1
            else:
                return True
        return False
            
            
                