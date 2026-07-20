class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        taskCount = [0] * 26

        for t in tasks:
            taskCount[ord(t) - ord('A')] +=1

        maxCount = max(taskCount)

        remainder = taskCount.count(maxCount)

        res = (maxCount -1) * (n + 1) + remainder

        return max(res, len(tasks))