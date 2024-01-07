"""
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.
 

Example 1:


Input: board = 
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: true
Example 2:

Input: board =
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: false
Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.

Constraints:

board.length == 9
board[i].length == 9
board[i][j] is a digit 1-9 or '.'.
"""
from itertools import product


class Solution:
    ROW_WIDTH = 9
    COLUMN_WIDTH = 9
    SQUARE_WIDTH = 3

    def isValidSudoku(self, board: list[list[str]]) -> bool:
        return self.is_row_valid(board) and self.is_column_valid(board) and self.is_square_valid(board)

    @staticmethod
    def check_if_duplicated(data: list[int]) -> bool:
        number_check_dict = {}

        for number in data:
            if number == ".":
                continue

            if number_check_dict.get(number):
                return False

            number_check_dict[number] = True

        return True

    def is_row_valid(self, board: list) -> bool:
        for row in board:
            if len(row) != self.ROW_WIDTH:
                return False

            valid = self.check_if_duplicated(row)
            if not valid:
                return False

        return True

    def is_column_valid(self, board: list) -> bool:
        for x in range(self.COLUMN_WIDTH):
            col = []
            for y in range(self.ROW_WIDTH):
                col.append(board[y][x])

            print(col)
            valid = self.check_if_duplicated(col)
            if not valid:
                return False

        return True

    def is_square_valid(self, board: list) -> bool:
        square_index = [list(range(3)), list(range(3, 6)), list(range(6, 9))]

        # possible x, y indexes
        for _px, _py in list(product(square_index, square_index)):
            squares = []
            for x in _px:
                for y in _py:
                    squares.append(board[x][y])

            valid = self.check_if_duplicated(squares)
            if not valid:
                return False

        return True


s = Solution()
board = [
    ["8", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"],
]

result = s.isValidSudoku(board)
print(result)  # expected = False


# Runtime 94 ms Beats 82.49% of users with Python3
# Memory 17.58 MB Beats 7.26% of users with Python3
