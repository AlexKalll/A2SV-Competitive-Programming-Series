class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        start, end  = 0, 0
        new_s = ""
        for n in spaces:
            end = n 
            new_s += s[start:end] + " "    
            start = n
        new_s += s[start:len(s)]
        return new_s
