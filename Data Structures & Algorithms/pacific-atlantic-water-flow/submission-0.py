class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        row = len(heights)
        col = len(heights[0])

        atlantic = set()
        pacific = set()

        def dfs(r,c, prevHeight, visited):
            if r < 0 or c < 0 or r == row or c == col:
                return

            if heights[r][c] >= prevHeight and (r,c) not in visited:
                visited.add((r,c))
            
                dfs(r + 1,c,heights[r][c], visited)
                dfs(r,c +1,heights[r][c], visited)
                dfs(r - 1,c,heights[r][c], visited)
                dfs(r,c -1,heights[r][c], visited)

        for r in range(row): dfs(r,0,heights[r][0], pacific)
        for c in range(col): dfs(0,c,heights[0][c], pacific)

        for r in reversed(range(row)): dfs(r,col-1,heights[r][col-1], atlantic)
        for c in reversed(range(col)): dfs(row-1,c,heights[row -1][c], atlantic)
                
        return [list(pair) for pair in atlantic & pacific]







            
            
