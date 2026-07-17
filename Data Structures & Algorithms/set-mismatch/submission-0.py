class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        visited = set()
        res = []

        for num in nums:
            if num in visited:
                res.append(num)
            else:
                visited.add(num)

        for num in range(1, len(nums) + 1):
            if num not in visited:
                res.append(num)
            

        return res
        



