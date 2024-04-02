class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        transpose = []
        for i in range(len(matrix[0])):
            innerlist = []
            for j in range(len(matrix)):
                innerlist.append(matrix[j][i])
            transpose.append(innerlist)
        return transpose
                
"""
# similarly
class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        transpose = []
        for i in range(len(matrix[0])):
            innerlist = []
            for row in matrix:
                innerlist.append(row[i])
            transpose.append(innerlist)
        return transpose

        """
"""
class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        res = [[0 for _ in range(len(matrix))] for _ in range(len(matrix[0]))]
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                res[col][row] = matrix[row][col]
        return res
"""
