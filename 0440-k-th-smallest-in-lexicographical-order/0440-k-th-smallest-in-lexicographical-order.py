class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        def countSteps(curr, n):
            steps = 0
            first, last = curr, curr
            while first <= n:
                steps += min(n, last) - first + 1
                first *= 10
                last = last * 10 + 9
            return steps
        
        curr = 1
        k -= 1  # we start from 1

        while k > 0:
            steps = countSteps(curr, n)
            if steps <= k:
                curr += 1
                k -= steps
            else:
                curr *= 10
                k -= 1

        return curr
