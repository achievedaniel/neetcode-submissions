class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i, v = 0, len(numbers) - 1

        while i < v:
            sum = numbers[i] + numbers[v]
            if sum == target:
                return[i + 1, v + 1]
            elif sum > target:
                v -= 1
            elif sum < target:
                i += 1

        return[]
        