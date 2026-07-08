class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        l, r = 0, 0
        result = 0
        total = 0

        while r < len(arr):
            total += arr[r]

            if r+1 - l == k:
                if total / k >= threshold:
                    result += 1
                total -= arr[l]
                l += 1

            r += 1
        
        return result