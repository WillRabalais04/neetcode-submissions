class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        col_digits = [[0] * 9 for _ in range(9)]
        squares = [[[0] * 9 for _ in range(3)] for _ in range(3)]
        print(squares)
        for row in range(0, 9):
            row_digits = [0] * 9
            for col in range(0, 9):
                box = board[row][col]
                if box != ".":
                    row_digits[int(box) - 1] += 1
                    col_digits[col][int(box) - 1] += 1
                    squares[row // 3][col // 3][int(box) - 1] += 1
            for digit in row_digits:
                if (digit > 1):
                    print(row_digits)
                    return False
        for col in col_digits:
            for digit in col:
                if (digit > 1):
                    print(col)
                    return False
        for row in squares:
            for col in row:
                for digit in col:
                    if (digit > 1):
                        return False
            
        return True

        




        