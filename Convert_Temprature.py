class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        kelvin = celsius + 273.15
        far = (9/5)* celsius + 32
        ans =[kelvin, far]
        return ans
