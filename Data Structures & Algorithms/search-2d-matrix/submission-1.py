class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])

        top, bot = 0, ROWS - 1#[top, bot]
        while top <= bot:#[top, bot]
            row = (top + bot) // 2
            if matrix[row][-1] < target:
                top = row + 1#[top, bot]
            elif matrix[row][0] > target:
                bot = row - 1
            else:
                break# means target in this col
        if top > bot:# loop end but we could not find a valid col
            return False

        left, right = 0, COLS - 1
        while left <= right:
            col = (left + right) // 2
            if matrix[row][col] < target:
                left = col + 1
            elif matrix[row][col] > target:
                right = col - 1
            else:
                return True
        return False
        
        