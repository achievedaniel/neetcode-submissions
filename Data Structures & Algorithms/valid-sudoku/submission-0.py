class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i, x in enumerate(board):
            row = set()
            for v, y in enumerate(x):
                test = str(i) + ':' + str(v)
                if y in row and y != ".":
                    return False
                else:
                    row.add(y)

        v = 0
        while v < len(board):
            columun = set()
            i = 0
            while i < len(board):
                if board[i][v] in columun and board[i][v] != ".":
                    return False
                else:
                    columun.add(board[i][v])
                i += 1
            v += 1

        v, i, y = 0, 0, 0
        square = set()
        while v < len(board) and i < len(board):
            if board[i][v] in square and board[i][v] != ".":
                return False
            else:
                square.add(board[i][v])
            v += 1
            if v % 3 == 0:
                i += 1
                v = y
            if v % 3 == 0 and i % 3 == 0:
                square = set()
            if i == 9:
                i = 0
                y += 3
                v = y

        return True