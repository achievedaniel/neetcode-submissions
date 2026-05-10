class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        sourcecolor = image[sr][sc]
        def dfs(r, c):
            if r < 0 or c < 0 or r == len(image) or c == len(image[0]):
                return
            if image[r][c] != sourcecolor:
                return

            image[r][c] = color

            dfs(r -1, c) #left
            dfs(r +1, c) #right
            dfs(r, c +1) #up
            dfs(r, c -1) #down

        if sourcecolor == color:
            return image
        
        dfs(sr,sc) 
        
        return image
    