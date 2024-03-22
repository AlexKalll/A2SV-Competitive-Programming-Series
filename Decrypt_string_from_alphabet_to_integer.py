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

# alos in java
"""
import java.util.HashMap;
import java.util.Map;

class Solution {
    public String freqAlphabets(String s) {
        // Initialize a map to map numbers (and numbers with '#') to letters
        Map<String, Character> m = new HashMap<>();
        for (int i = 1; i < 10; i++) {
            m.put(String.valueOf(i), (char) (96 + i));
        }
        for (int i = 10; i < 27; i++) {
            m.put(String.valueOf(i) + '#', (char) (96 + i));
        }

        StringBuilder res = new StringBuilder();
        int i = 0;
        int n = s.length();

        while (i < n) {
            // If the current index is part of a 10# to 26# pattern
            if (i + 2 < n && s.charAt(i + 2) == '#') {
                res.append(m.get(s.substring(i, i + 3)));
                i += 3;
            } else {
                res.append(m.get(String.valueOf(s.charAt(i)));
                i++;
            }
        }

        return res.toString();
    }
}
""""
