class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        vis = set()

        for i in nums:
            if i in vis:
                return True
            vis.add(i)
        return False