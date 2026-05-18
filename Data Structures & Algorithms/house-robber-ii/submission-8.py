class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        def robFun(r):
            if len(r) == 1:
                return r[0]
            
            dp = [0] * len(r)
            dp[0] = r[0]
            dp[1] = max(r[0], r[1])

            for i in range(2, len(r)):
                dp[i] = max(dp[i-1], r[i] + dp[i-2])

            return dp[-1]

        return max(robFun(nums[:-1]), robFun(nums[1:]))