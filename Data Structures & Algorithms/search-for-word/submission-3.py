class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row = (len(board))
        collumn = (len(board[0]))
        def findWord(r, c, i):
            if i == len(word):
                return True
            
            if r < 0 or c < 0 or r == row or c == collumn or board[r][c] != word[i]:
                return False
            
            board[r][c] = "#"

            found = (
                findWord(r +1,c,i +1) or
                findWord(r -1,c,i +1) or
                findWord(r,c +1,i +1) or
                findWord(r,c -1,i +1)
            )

            board[r][c] = word[i]

            return found

        for r in range(row):
            for c in range(collumn):
                if findWord(r, c, 0):
                    return True

        return False


             

            

        