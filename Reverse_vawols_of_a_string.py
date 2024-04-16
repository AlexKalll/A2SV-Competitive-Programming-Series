class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ['a' , 'e' , 'i' ,  'o' , 'u' ,'A' ,'I', 'O' ,'U','E']
        n = len(s)
        a = list(s)
        i, j = 0, n - 1
        while i < j:
            if a[i] in vowels and a[j] in vowels:
                a[i], a[j] = a[j], a[i]
                i += 1
                j -= 1
            if a[i] not in vowels:
                i += 1
            if a[j] not in vowels:
                j -= 1
        reversd_str = "".join(a)
        return reversd_str 
            
