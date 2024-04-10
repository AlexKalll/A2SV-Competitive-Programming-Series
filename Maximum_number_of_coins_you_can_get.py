class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        n = len(piles)
        piles.sort()
        my_total_coins = 0
        start = n/3
        start = int(start) # start = n//3
        while start < n:
            my_total_coins += piles[start]
            start += 2
        return my_total_coins
