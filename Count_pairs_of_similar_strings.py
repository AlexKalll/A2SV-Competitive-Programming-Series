class Solution:
    def similarPairs(self, words: List[str]) -> int:
        count = 0
        N = len(words)

        for i in range(N):
            for j in range(i+1, N):  #This iterates from 1th to the N-1th elements   , that makes sense
                if set(words[i]) == set(words[j]):
                    count += 1
        return count
