class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        used = {n: False for n in nums}

        def dfs(path):
            if len(nums) == len(path):
                res.append(path.copy())
                return
            
            for num in nums:
                if used[num]:
                    continue
                
                path.append(num)
                used[num] = True

                dfs(path)
            
                used[num] = False
                path.pop()
        
        dfs([])

        return res

        