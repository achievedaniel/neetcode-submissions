class Solution:
    def solve(self, board: List[List[str]]) -> None:
        col = len(board[0])
        row = len(board)

        visited = set()

        def dfs(r,c):
            if r < 0 or c < 0 or c == col or r == row:
                return

            if board[r][c] == "O" and (r,c) not in visited:
                visited.add((r,c))
            
                dfs(r +1,c)
                dfs(r -1,c)
                dfs(r,c +1)
                dfs(r,c -1)

        for r in range(row): dfs(r,0)
        for c in range(col): dfs(0,c)
        for r in reversed(range(row)): dfs(r,col -1)
        for c in reversed(range(col)): dfs(row -1, c)

        for c in range(col):
            for r in range(row):
                if board[r][c] == "O" and (r,c) not in visited:
                    board[r][c] = "X"

        