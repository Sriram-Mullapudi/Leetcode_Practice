class Solution:
    def findDiagonalOrder(self, mat):
        if not mat or not mat[0]:
            return []
        
        m, n = len(mat), len(mat[0])
        result = []
        
        for d in range(m + n - 1):  # number of diagonals
            intermediate = []
            
            # Determine the starting row for this diagonal
            r = 0 if d < n else d - n + 1
            c = d if d < n else n - 1
            
            # Collect elements in this diagonal
            while r < m and c >= 0:
                intermediate.append(mat[r][c])
                r += 1
                c -= 1
            
            # If diagonal index is even, reverse it
            if d % 2 == 0:
                result.extend(intermediate[::-1])
            else:
                result.extend(intermediate)
        
        return result
