class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numCount = defaultdict(int)

        for i in nums:
            numCount[i] += 1

        bucket = [[] for i in range(len(nums) + 1)]

        for num, cnt in numCount.items():
            bucket[cnt].append(num)
        result = []

        for i in reversed(bucket):
                for x in i:
                    result.append(x)
                    if len(result) == k:
                        return result
        