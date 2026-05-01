class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        curMax = -1
        for i in range(len(arr) -1, -1, -1):
            newMax = arr[i]
            arr[i] = curMax
            curMax = max(curMax, newMax)
        return arr

