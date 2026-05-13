class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        used = {i: False for i in range(len(nums))}
        nums.sort()

        def dfs(path):
            if len(path) == len(nums):
                res.append(path.copy())
                return

            for i in range(len(nums)):
                if i >0 and nums[i] == nums[i-1] and not used[i-1] or used[i]:
                    continue
                
                path.append(nums[i])
                used[i] = True

                dfs(path)
                used[i] = False

                path.pop()
        

        dfs([])
        return res
