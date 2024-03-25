'''
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
'''
from defaultlist import defaultlist
from collections import defaultdict

class Solution:
    def check_duplicates(self, row):
        board = self.board
        for elements in row:
            data = set()
            for entry in elements:
                entry = board[entry[0]][entry[1]]
                if "." == entry:
                    continue
                elif entry in data:
                    print(data)
                    print(entry)
                    return False
                else:
                    data.add(entry)
        return True

    def isValidSudoku(self, board) -> bool:
        self.board = board
        row_entries = defaultlist(lambda: [])
        column_entries = defaultlist(lambda: [])
        box_entries = defaultlist(lambda: [])
        for row in range(len(board)):
            multiple = 1
            for column in range(len(board[row])):
                row_entries[row].append([row, column])
                column_entries[row].append([column, row])
                box_number = (row // 3) * 3 + column // 3
                # if multiple < 3:
                #     box_entries[box].append([row, column])
                #     multiple += 1
                # else:
                #     multiple = 0
                #     box += 1   

        print(row_entries)
        print(self.check_duplicates(row_entries))
        print(self.check_duplicates(column_entries))

    def isValidNew(self, board):
        row_set = defaultdict(set)
        column_set = defaultdict(set)
        box_set = defaultdict(set)
        for row in range(9):
            for column in range(9):
                value = board[row][column]
                if value == ".":
                    continue
                if (value in row_set[row] or 
                    value in column_set[column] or
                    value in box_set[(row//3, column//3)]):
                    return False
                else:
                    row_set[row].add(value)
                    column_set[column].add(value)
                    box_set[(row//3, column//3)].add(value)
        else:
            return True

print(Solution().isValidNew([["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]))