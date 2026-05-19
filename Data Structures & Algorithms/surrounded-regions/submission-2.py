class Solution:
    def solve(self, board: List[List[str]]) -> None:
        col = len(board[0])
        row = len(board)

        visited = set()

        def dfs(r,c):
            if r < 0 or c < 0 or r == row or c == col:
                return
            if board[r][c] == "X":
                return
            if (r,c) in visited:
                return

            visited.add((r,c))
            dfs(r +1,c)
            dfs(r -1,c)
            dfs(r,c +1)
            dfs(r,c -1)

        for r in range(row): dfs(r,0)
        for r in range(row): dfs(r,col-1)
        for c in range(col): dfs(0,c)
        for c in range(col): dfs(row-1,c)

        for c in range(col):
            for r in range(row):
                if (r,c) not in visited:
                    board[r][c] = "X"
        
        
