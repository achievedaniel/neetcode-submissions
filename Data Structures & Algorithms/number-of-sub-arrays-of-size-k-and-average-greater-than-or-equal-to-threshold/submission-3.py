class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        l, r = 0, 0
        result = 0
        total = 0
        average = 0

        while r < len(arr):
            total += arr[r]
            average = total / k

            if r+1 - l == k:
                if average >= threshold:
                    result += 1
                total -= arr[l]
                l += 1

            r += 1
        
        return result