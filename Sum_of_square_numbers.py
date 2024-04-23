class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        first, second = 0, int(math.sqrt(c))
        while first <= second:
            product = first**2 + second**2
            if product == c:
                return True 
            elif product < c:
                first += 1
            else:
                second -= 1
        return False
