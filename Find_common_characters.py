class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        result = []
    # Initialize a dictionary to store character frequencies
        char_count = {}

        # Initialize the character count based on the first word
        for char in words[0]:
            char_count[char] = char_count.get(char, 0) + 1
        
        # Iterate through the remaining words
        for word in words[1:]:
            temp_count = {}
            for char in word:
                temp_count[char] = temp_count.get(char, 0) + 1
            
            # Update the character count by taking the minimum occurrence
            for char in char_count:
                char_count[char] = min(char_count[char], temp_count.get(char, 0))
        
        for char, freq in char_count.items():
            result.extend([char] * freq)
        
        return result

        """
        #This is very easy one
class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        k=words[0]
        list1=[]
        for x in k:
            n=0
            for i,y in enumerate(words):
                if x in y:
                    n+=1
                    words[i]=y.replace(x,"",1)
            if n==len(words):
                list1.append(x)
        return(list1)
        """
