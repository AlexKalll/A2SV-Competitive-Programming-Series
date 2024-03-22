class Solution:
    def freqAlphabets(self, s: str) -> str:
        # Initialize a dictionary to map numbers (and numbers with '#') to letters
        m = {str(i): chr(96 + i) for i in range(1, 10)}
        m.update({str(i) + '#': chr(96 + i) for i in range(10, 27)})
        
        res = ""
        i = 0
        n = len(s)

        while i < n:
         # If the current index is part of a 10# to 26# pattern
            if i + 2 < n and s[i + 2] == '#':
                res += m[s[i:i+3]] 
                i += 3 
            else:
                res += m[s[i]]  
                i += 1  
                
        return res
