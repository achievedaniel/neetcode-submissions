class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        path = []
        def dfs(n, total):
            if total == target:
                res.append(path.copy())
                return

            if total > target or n == len(nums):
                return

            path.append(nums[n])
            dfs(n, total + nums[n])
            path.pop()

            dfs(n + 1, total)

        dfs(0, 0)
        return res


            
