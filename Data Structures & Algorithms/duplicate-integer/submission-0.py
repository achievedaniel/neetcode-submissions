class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        vis = set()

        for i in nums:
            if i not in vis:
                vis.add(i)
            else:
                return True
        return False