class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = 0
        if n == 0:
            return True
        if len(flowerbed) == 1:
            return True if flowerbed[0] == 0 else False
        for i in range(len(flowerbed)):
            if flowerbed[i] == 0:
                if i == 0 and flowerbed[i +1] == 0:
                    count += 1
                    flowerbed[i] = 1
                elif i == len(flowerbed) - 1 and flowerbed[i - 1] == 0:
                    count += 1
                    flowerbed[i] = 1
                elif flowerbed[i -1] == 0 and flowerbed[i +1] == 0:
                    count += 1
                    flowerbed[i] = 1
        
        return True if count >= n else False