from typing import List

class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        m, n = len(matrix), len(matrix[0])
        prev = [0] * (n + 1)  # dp for previous row (1-based padded)
        ans = 0
        for i in range(1, m + 1):
            curr = [0] * (n + 1)
            for j in range(1, n + 1):
                if matrix[i-1][j-1] == 1:
                    curr[j] = 1 + min(curr[j-1], prev[j], prev[j-1])
                    ans += curr[j]
            prev = curr
        return ans
