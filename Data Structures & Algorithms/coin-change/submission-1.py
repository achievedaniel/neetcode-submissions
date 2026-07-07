class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        change = [amount +1] * (amount +1)

        change[0] = 0

        for i in range(1, amount +1):
            for coin in coins:
                if coin <= i:
                    change[i] = min(change[i], change[i - coin] +1)

        return -1 if change[-1] == amount +1 else change[-1]