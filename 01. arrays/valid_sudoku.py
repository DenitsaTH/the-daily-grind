class Solution:
    def isValidSudoku(self, board) -> bool:
        rows, cols = 9,9
        

        for i in range(rows):
            control_set = set()
            for j in range(cols):
                if not board[i][j].isdigit():
                    continue
                if board[i][j] in control_set:
                    return False
                else:
                    control_set.add(board[i][j])


        for i in range(cols):
            control_set = set()
            for j in range(rows):
                if not board[j][i].isdigit():
                    continue
                if board[j][i] in control_set:
                    return False
                else:
                    control_set.add(board[j][i])


        for row in range(0, rows, 3):
            for col in range(0, cols, 3):
                control_set = set()
                for j in range(3):
                    for k in range(3):

                        if not board[j+row][k+col].isdigit():
                            continue
                        if board[j+row][k+col] in control_set:
                            return False
                        else:
                            control_set.add(board[j+row][k+col])

        return True
